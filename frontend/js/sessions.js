const Sessions = {

    allSessions: [],
    languages: [],
    skills: [],
    routines: [],

    async loadData() {
        this.allSessions = await api.getSessions();
        this.languages = await api.getLanguages();
        this.skills = await api.getSkills();
        this.routines = await api.getRoutines();
    },

    getLanguageName(routineId) {
        const routine = this.routines.find(r => r.id === routineId);
        if (!routine) return "—";
        const lang = this.languages.find(l => l.id === routine.language_id);
        return lang ? lang.name : "—";
    },

    getSkillName(routineId) {
        const routine = this.routines.find(r => r.id === routineId);
        if (!routine) return "—";
        const skill = this.skills.find(s => s.id === routine.skill_id);
        return skill ? skill.name : "—";
    },

    async render(filter = "all") {
        await this.loadData();

        const container = document.getElementById("all-sessions");
        let sessions = [...this.allSessions];

        if (filter === "completed") {
            sessions = sessions.filter(s => s.completed);
        } else if (filter === "pending") {
            sessions = sessions.filter(s => !s.completed);
        }

        if (sessions.length === 0) {
            container.innerHTML = `
                <div class="empty-state">
                    <i class="ti ti-book"></i>
                    <p>No sessions found.</p>
                </div>
            `;
            return;
        }

        const grouped = {};
        sessions.forEach(session => {
            const date = session.date;
            if (!grouped[date]) grouped[date] = [];
            grouped[date].push(session);
        });

        const sortedDates = Object.keys(grouped).sort((a, b) => new Date(b) - new Date(a));

        let html = "";
        sortedDates.forEach(date => {
            const dateObj = new Date(date + "T12:00:00");
            const formatted = dateObj.toLocaleDateString("en-US", {
                month: "long", day: "numeric", weekday: "long"
            });
            html += `<div class="date-divider">${formatted}</div>`;

            grouped[date].forEach(session => {
                html += this.renderCard(session);
            });
        });

        container.innerHTML = html;
    },

    renderCard(session) {
        const langName = this.getLanguageName(session.routine_id);
        const skillName = this.getSkillName(session.routine_id);
        const completedClass = session.completed ? "completed" : "";
        const checkboxClass = session.completed ? "checked" : "";
        const checkIcon = session.completed ? '<i class="ti ti-check"></i>' : "";

        let summaryHtml = "";
        if (session.summary && session.completed) {
            summaryHtml = `
                <div class="session-summary">
                    <div class="session-summary-label">Summary</div>
                    <div class="session-summary-text">${session.summary}</div>
                </div>
            `;
        }

        return `
            <div class="session-card ${completedClass}" data-id="${session.id}">
                <div class="session-checkbox ${checkboxClass}" onclick="Sessions.toggleComplete(${session.id}, ${!session.completed})">
                    ${checkIcon}
                </div>
                <div class="session-info">
                    <div class="session-material" ${!session.material ? `onclick="Sessions.editSession(${session.id})"` : ""}>
                        ${session.material ? session.material : '<span class="material-placeholder">Click to add study material...</span>'}
                    </div>
                    <div class="session-tags">
                        <span class="tag language">${langName}</span>
                        <span class="tag skill">${skillName}</span>
                    </div>
                    ${summaryHtml}
                    <div class="summary-expand" id="summary-${session.id}" style="display: none;">
                        <textarea id="summary-text-${session.id}" placeholder="What did you learn? (optional)"></textarea>
                        <div class="summary-actions">
                            <button class="btn-secondary" onclick="Sessions.completeWithoutSummary(${session.id})">Skip</button>
                            <button class="btn-primary" onclick="Sessions.completeWithSummary(${session.id})">Save</button>
                        </div>
                    </div>
                </div>
                <div class="session-actions">
                    <button class="btn-icon" onclick="Sessions.editSession(${session.id})">
                        <i class="ti ti-pencil"></i>
                    </button>
                    <button class="btn-icon" onclick="Sessions.removeSession(${session.id})">
                        <i class="ti ti-trash"></i>
                    </button>
                </div>
            </div>
        `;
    },

    async toggleComplete(id, completed) {
        const session = this.allSessions.find(s => s.id === id);
        if (!session) return;

        if (completed) {
            document.getElementById(`summary-${id}`).style.display = "block";
        } else {
            await api.updateSession(id, session.routine_id, session.date, session.material, false, null);
            App.showToast("Session updated!");
            this.render();
            Routine.render();
        }
    },

    async completeWithoutSummary(id) {
        const session = this.allSessions.find(s => s.id === id);
        if (!session) return;

        await api.updateSession(id, session.routine_id, session.date, session.material, true, session.summary);
        App.showToast("Session completed!");
        this.render();
        Routine.render();
    },

    async completeWithSummary(id) {
        const session = this.allSessions.find(s => s.id === id);
        if (!session) return;

        const summary = document.getElementById(`summary-text-${id}`).value.trim() || null;
        await api.updateSession(id, session.routine_id, session.date, session.material, true, summary);
        App.showToast("Session completed!");
        this.render();
        Routine.render();
    },

    editSession(id) {
        const session = this.allSessions.find(s => s.id === id);
        if (!session) return;

        const title = document.getElementById("modal-title");
        const body = document.getElementById("modal-body");

        title.textContent = "Edit session";
        body.innerHTML = `
            <div class="form-group">
                <label>Material</label>
                <input type="text" id="edit-material" value="${session.material}">
            </div>
            <div class="form-group">
                <label>Summary</label>
                <textarea id="edit-summary">${session.summary || ""}</textarea>
            </div>
            <div class="form-actions">
                <button class="btn-secondary" onclick="App.closeModal()">Cancel</button>
                <button class="btn-primary" onclick="Sessions.updateSession(${id})">Save</button>
            </div>
        `;

        App.openModal();
    },

    async updateSession(id) {
        const session = this.allSessions.find(s => s.id === id);
        const material = document.getElementById("edit-material").value.trim();
        const summary = document.getElementById("edit-summary").value.trim() || null;

        if (!material) return;

        await api.updateSession(id, session.routine_id, session.date, material, session.completed, summary);
        App.closeModal();
        App.showToast("Session updated!");
        await this.render();
        await Routine.render();
    },

    async removeSession(id) {
        if (!confirm("Delete this session?")) return;
        await api.deleteSession(id);
        this.render();
        Routine.render();
        App.showToast("Session deleted!")
    }
};