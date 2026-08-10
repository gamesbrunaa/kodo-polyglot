const App = {

    init() {
        this.setupTabs();
        this.setupModal();
        this.setupFilters();

        Routine.render();
        Routine.renderRoutineList();
    },

    setupTabs() {
        document.querySelectorAll(".menu-item").forEach(item => {
            item.addEventListener("click", () => {
                const tab = item.dataset.tab;
                this.switchTab(tab);
            });
        });
    },

    switchTab(tab) {
        document.querySelectorAll(".menu-item").forEach(item => {
            item.classList.toggle("active", item.dataset.tab === tab);
        });

        document.querySelectorAll(".tab-content").forEach(section => {
            section.classList.toggle("active", section.id === tab);
        });

        switch (tab) {
            case "routine":
                Routine.render();
                Routine.renderRoutineList();
                break;
            case "sessions":
                Sessions.render();
                break;
            case "languages":
                Language.render();
                break;
            case "skills":
                Skills.render();
                break;
        }
    },

    setupModal() {
        document.getElementById("modal-overlay").addEventListener("click", (e) => {
            if (e.target === e.currentTarget) {
                this.closeModal();
            }
        });
    },

    openModal() {
        document.getElementById("modal-overlay").classList.add("active");
    },

    closeModal() {
        document.getElementById("modal-overlay").classList.remove("active");
    },

    setupFilters() {
        document.querySelectorAll(".filter-pills .pill").forEach(pill => {
            pill.addEventListener("click", () => {
                document.querySelectorAll(".filter-pills .pill").forEach(p => p.classList.remove("active"));
                pill.classList.add("active");
                Sessions.render(pill.dataset.filter);
            });
        });
    }
};

document.addEventListener("DOMContentLoaded", () => {
    App.init();
});