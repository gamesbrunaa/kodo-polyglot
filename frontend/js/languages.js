const Language = {

    async render() {
        const container = document.getElementById("languages-list");
        const languages = await api.getLanguages();

        if (languages.length === 0) {
            container.innerHTML = `
                <div class="empty-state" style="grid-column: 1 / -1;">
                    <i class="ti ti-world"></i>
                    <p>No languages yet. Add your first one!</p>
                </div>
            `;
            return;
        }

        container.innerHTML = languages.map(lang => `
            <div class="entity-card" data-id="${lang.id}">
                <div class="entity-card-actions">
                    <button class="btn-icon" onclick="Language.edit(${lang.id}, '${lang.name}', '${lang.level || ''}')">
                        <i class="ti ti-pencil"></i>
                    </button>
                    <button class="btn-icon" onclick="Language.remove(${lang.id})">
                        <i class="ti ti-trash"></i>
                    </button>
                </div>
                <div class="entity-card-name">${lang.name}</div>
                ${lang.level ? `<span class="entity-card-level">${lang.level}</span>` : '<span class="entity-card-detail">No level set</span>'}
            </div>
        `).join("");
    },

    showAddModal() {
        const title = document.getElementById("modal-title");
        const body = document.getElementById("modal-body");

        title.textContent = "Add language";
        body.innerHTML = `
            <div class="form-group">
                <label>Name</label>
                <input type="text" id="lang-name" placeholder="e.g. Français, English">
            </div>
            <div class="form-group">
                <label>Level (optional)</label>
                <input type="text" id="lang-level" placeholder="e.g. A1, B2">
            </div>
            <div class="form-actions">
                <button class="btn-secondary" onclick="App.closeModal()">Cancel</button>
                <button class="btn-primary" onclick="Language.save()">Save</button>
            </div>
        `;

        App.openModal();
    },

    async save() {
        const name = document.getElementById("lang-name").value.trim();
        const level = document.getElementById("lang-level").value.trim() || null;

        if (!name) return;

        await api.createLanguage(name, level);
        App.closeModal();
        Language.render();
    },

    edit(id, name, level) {
        const title = document.getElementById("modal-title");
        const body = document.getElementById("modal-body");

        title.textContent = "Edit language";
        body.innerHTML = `
            <div class="form-group">
                <label>Name</label>
                <input type="text" id="lang-name" value="${name}">
            </div>
            <div class="form-group">
                <label>Level</label>
                <input type="text" id="lang-level" value="${level}">
            </div>
            <div class="form-actions">
                <button class="btn-secondary" onclick="App.closeModal()">Cancel</button>
                <button class="btn-primary" onclick="Language.update(${id})">Save</button>
            </div>
        `;

        App.openModal();
    },

    async update(id) {
        const name = document.getElementById("lang-name").value.trim();
        const level = document.getElementById("lang-level").value.trim() || null;

        if (!name) return;

        await api.updateLanguage(id, name, level);
        App.closeModal();
        Language.render();
    },

    async remove(id) {
        if (!confirm("Delete this language?")) return;
        await api.deleteLanguage(id);
        Language.render();
    }
};