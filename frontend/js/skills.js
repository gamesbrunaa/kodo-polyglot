const Skills = {

    async render() {
        const container = document.getElementById("skills-list");
        const skills = await api.getSkills();

        if (skills.length === 0) {
            container.innerHTML = `
                <div class="empty-state" style="grid-column: 1 / -1;">
                    <i class="ti ti-target"></i>
                    <p>No skills yet. Add your first one!</p>
                </div>
            `;
            return;
        }

        container.innerHTML = skills.map(skill => `
            <div class="entity-card" data-id="${skill.id}">
                <div class="entity-card-actions">
                    <button class="btn-icon" onclick="Skills.edit(${skill.id}, '${skill.name}')">
                        <i class="ti ti-pencil"></i>
                    </button>
                    <button class="btn-icon" onclick="Skills.remove(${skill.id})">
                        <i class="ti ti-trash"></i>
                    </button>
                </div>
                <div class="entity-card-name">${skill.name}</div>
            </div>
        `).join("");
    },

    showAddModal() {
        const title = document.getElementById("modal-title");
        const body = document.getElementById("modal-body");

        title.textContent = "Add skill";
        body.innerHTML = `
            <div class="form-group">
                <label>Name</label>
                <input type="text" id="skill-name" placeholder="e.g. Reading, Speaking">
            </div>
            <div class="form-actions">
                <button class="btn-secondary" onclick="App.closeModal()">Cancel</button>
                <button class="btn-primary" onclick="Skills.save()">Save</button>
            </div>
        `;

        App.openModal();
    },

    async save() {
        const name = document.getElementById("skill-name").value.trim();
        if (!name) return;

        await api.createSkill(name);
        App.closeModal();
        Skills.render();
    },

    edit(id, name) {
        const title = document.getElementById("modal-title");
        const body = document.getElementById("modal-body");

        title.textContent = "Edit skill";
        body.innerHTML = `
            <div class="form-group">
                <label>Name</label>
                <input type="text" id="skill-name" value="${name}">
            </div>
            <div class="form-actions">
                <button class="btn-secondary" onclick="App.closeModal()">Cancel</button>
                <button class="btn-primary" onclick="Skills.update(${id})">Save</button>
            </div>
        `;

        App.openModal();
    },

    async update(id) {
        const name = document.getElementById("skill-name").value.trim();
        if (!name) return;

        await api.updateSkill(id, name);
        App.closeModal();
        Skills.render();
    },

    async remove(id) {
        if (!confirm("Delete this skill?")) return;
        await api.deleteSkill(id);
        Skills.render();
    }
};