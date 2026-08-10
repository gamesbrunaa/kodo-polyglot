const Routine = {

    currentDate: new Date(),

    async render() {
        await Sessions.loadData();

        const dayName = this.currentDate.toLocaleDateString("en-US", { weekday: "long" });
        const dateStr = this.currentDate.toLocaleDateString("en-US", { month: "long", day: "numeric", year: "numeric" });

        document.getElementById("routine-day").textContent = dayName;
        document.getElementById("routine-date").textContent = dateStr;
        document.getElementById("date-picker").value = this.currentDate.toISOString().split("T")[0];

        const today = new Date();
        const isToday = this.currentDate.toDateString() === today.toDateString();
        document.getElementById("today-badge").style.display = isToday ? "inline-block" : "none";

        const total = Sessions.allSessions.length;
        const completed = Sessions.allSessions.filter(s => s.completed).length;

        document.getElementById("total-sessions").textContent = total;
        document.getElementById("completed-sessions").textContent = completed;
        document.getElementById("streak-count").textContent = this.calculateStreak();

        const dateISO = this.currentDate.toISOString().split("T")[0];
        const daySessions = Sessions.allSessions.filter(s => s.date === dateISO);

        const container = document.getElementById("routine-sessions");

        if (daySessions.length === 0) {
            container.innerHTML = `
                <div class="empty-state">
                    <i class="ti ti-calendar"></i>
                    <p>No sessions for ${isToday ? "today" : dayName.toLowerCase()}.</p>
                </div>
            `;
            return;
        }

        container.innerHTML = daySessions.map(session => Sessions.renderCard(session)).join("");
    },

    prevDay() {
        this.currentDate.setDate(this.currentDate.getDate() - 1);
        this.render();
    },

    nextDay() {
        this.currentDate.setDate(this.currentDate.getDate() + 1);
        this.render();
    },

    goToday() {
        this.currentDate = new Date();
        this.render();
    },

    goToDate(dateStr) {
        this.currentDate = new Date(dateStr + "T12:00:00");
        this.render();
    },

    calculateStreak() {
        const dates = [...new Set(
            Sessions.allSessions
                .filter(s => s.completed)
                .map(s => s.date)
        )].sort((a, b) => new Date(b) - new Date(a));

        if (dates.length === 0) return 0;

        let streak = 1;
        for (let i = 0; i < dates.length - 1; i++) {
            const current = new Date(dates[i]);
            const prev = new Date(dates[i + 1]);
            const diff = (current - prev) / (1000 * 60 * 60 * 24);
            if (diff === 1) {
                streak++;
            } else {
                break;
            }
        }
        return streak;
    },

    async showAddSessionModal() {
        await Sessions.loadData();

        const title = document.getElementById("modal-title");
        const body = document.getElementById("modal-body");
        const modal = document.querySelector(".modal");
        modal.classList.remove("modal-lg");

        if (Sessions.routines.length === 0) {
            title.textContent = "No routines yet";
            body.innerHTML = `
                <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 16px;">
                    You need to create a routine first. Go to "Manage routines" to set up your weekly plan.
                </p>
                <div class="form-actions">
                    <button class="btn-secondary" onclick="App.closeModal()">Cancel</button>
                    <button class="btn-primary" onclick="App.closeModal(); Routine.showManageModal()">Manage routines</button>
                </div>
            `;
            App.openModal();
            return;
        }

        const routineOptions = Sessions.routines.map(r => {
            const lang = Sessions.languages.find(l => l.id === r.language_id);
            const skill = Sessions.skills.find(s => s.id === r.skill_id);
            const label = `${r.day_of_week} — ${lang ? lang.name : "?"} — ${skill ? skill.name : "?"}`;
            return `<option value="${r.id}">${label}</option>`;
        }).join("");

        const selectedDate = this.currentDate.toISOString().split("T")[0];

        title.textContent = "New study session";
        body.innerHTML = `
            <div class="form-group">
                <label>Routine</label>
                <select id="session-routine">
                    <option value="">Select a routine</option>
                    ${routineOptions}
                </select>
            </div>
            <div class="form-group">
                <label>Date</label>
                <input type="date" id="session-date" value="${selectedDate}">
            </div>
            <div class="form-group">
                <label>Material</label>
                <input type="text" id="session-material" placeholder="e.g. Read chapter 5, Watch video...">
            </div>
            <div class="form-actions">
                <button class="btn-secondary" onclick="App.closeModal()">Cancel</button>
                <button class="btn-primary" onclick="Routine.saveSession()">Save</button>
            </div>
        `;

        App.openModal();
    },

    async saveSession() {
        const routineId = parseInt(document.getElementById("session-routine").value);
        const date = document.getElementById("session-date").value;
        const material = document.getElementById("session-material").value.trim();

        if (!routineId || !date || !material) return;

        await api.createSession(routineId, date, material, false, null);
        App.closeModal();
        Routine.render();
    },

    async showManageModal() {
        const languages = await api.getLanguages();
        const skills = await api.getSkills();
        const routines = await api.getRoutines();

        const title = document.getElementById("modal-title");
        const body = document.getElementById("modal-body");
        const modal = document.querySelector(".modal");
        modal.classList.add("modal-lg");

        title.textContent = "Weekly routine";

        if (languages.length === 0 || skills.length === 0) {
            body.innerHTML = `
                <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 16px;">
                    You need at least one language and one skill first. Go to the Languages and Skills tabs to add them.
                </p>
                <div class="form-actions">
                    <button class="btn-primary" onclick="App.closeModal()">Got it</button>
                </div>
            `;
            App.openModal();
            return;
        }

        const days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];

        const langOptions = languages.map(l =>
            `<option value="${l.id}">${l.name}${l.level ? " (" + l.level + ")" : ""}</option>`
        ).join("");

        const skillOptions = skills.map(s =>
            `<option value="${s.id}">${s.name}</option>`
        ).join("");

        const dayOptions = days.map(d => `<option value="${d}">${d}</option>`).join("");

        let weekHtml = "";
        days.forEach(day => {
            const dayRoutines = routines.filter(r => r.day_of_week === day);

            let itemsHtml = "";
            if (dayRoutines.length > 0) {
                itemsHtml = dayRoutines.map(r => {
                    const lang = languages.find(l => l.id === r.language_id);
                    const skill = skills.find(s => s.id === r.skill_id);
                    return `
                        <div class="manage-routine-item">
                            <div class="manage-routine-tags">
                                <span class="tag language">${lang ? lang.name : "?"}</span>
                                <span class="tag skill">${skill ? skill.name : "?"}</span>
                            </div>
                            <button class="btn-icon" onclick="Routine.removeRoutine(${r.id})">
                                <i class="ti ti-trash"></i>
                            </button>
                        </div>
                    `;
                }).join("");
            } else {
                itemsHtml = `<div class="manage-routine-empty">No routines</div>`;
            }

            weekHtml += `
                <div class="manage-day">
                    <div class="manage-day-label">${day}</div>
                    <div class="manage-day-items">${itemsHtml}</div>
                </div>
            `;
        });

        body.innerHTML = `
            <div class="manage-add-form">
                <div class="manage-add-row">
                    <select id="routine-day-select">${dayOptions}</select>
                    <select id="routine-language">${langOptions}</select>
                    <select id="routine-skill">${skillOptions}</select>
                    <button class="btn-primary" onclick="Routine.saveRoutine()">
                        <i class="ti ti-plus"></i> Add
                    </button>
                </div>
            </div>
            <div class="manage-week">${weekHtml}</div>
        `;

        App.openModal();
    },

    async saveRoutine() {
        const day = document.getElementById("routine-day-select").value;
        const languageId = parseInt(document.getElementById("routine-language").value);
        const skillId = parseInt(document.getElementById("routine-skill").value);

        if (!day || !languageId || !skillId) return;

        await api.createRoutine(day, languageId, skillId);
        Routine.showManageModal();
    },

    async removeRoutine(id) {
        if (!confirm("Delete this routine?")) return;
        await api.deleteRoutine(id);
        Routine.showManageModal();
    }
};