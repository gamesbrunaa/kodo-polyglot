const API_URL = "http://localhost:8000";

const api = {

    async getLanguages() {
        const response = await fetch(`${API_URL}/languages`);
        return response.json();
    },

    async createLanguage(name, level) {
        const response = await fetch(`${API_URL}/languages`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name, level })
        });
        return response.json();
    },

    async updateLanguage(id, name, level) {
        const response = await fetch(`${API_URL}/languages/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name, level })
        });
        return response.json();
    },

    async deleteLanguage(id) {
        await fetch(`${API_URL}/languages/${id}`, { method: "DELETE" });
    },

    async getSkills() {
        const response = await fetch(`${API_URL}/skills`);
        return response.json();
    },

    async createSkill(name) {
        const response = await fetch(`${API_URL}/skills`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name })
        });
        return response.json();
    },

    async updateSkill(id, name) {
        const response = await fetch(`${API_URL}/skills/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name })
        });
        return response.json();
    },

    async deleteSkill(id) {
        await fetch(`${API_URL}/skills/${id}`, { method: "DELETE" });
    },

    async getRoutines() {
        const response = await fetch(`${API_URL}/routines`);
        return response.json();
    },

    async createRoutine(day_of_week, language_id, skill_id) {
        const response = await fetch(`${API_URL}/routines`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ day_of_week, language_id, skill_id })
        });
        return response.json();
    },

    async updateRoutine(id, day_of_week, language_id, skill_id) {
        const response = await fetch(`${API_URL}/routines/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ day_of_week, language_id, skill_id })
        });
        return response.json();
    },

    async deleteRoutine(id) {
        await fetch(`${API_URL}/routines/${id}`, { method: "DELETE" });
    },

    async getSessions() {
        const response = await fetch(`${API_URL}/studysessions`);
        return response.json();
    },

    async createSession(routine_id, date, material, completed, summary) {
        const response = await fetch(`${API_URL}/studysessions`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ routine_id, date, material, completed, summary })
        });
        return response.json();
    },

    async updateSession(id, routine_id, date, material, completed, summary) {
        const response = await fetch(`${API_URL}/studysessions/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ routine_id, date, material, completed, summary })
        });
        return response.json();
    },

    async deleteSession(id) {
        await fetch(`${API_URL}/studysessions/${id}`, { method: "DELETE" });
    }
};