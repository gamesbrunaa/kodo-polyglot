class StudySessionService:
    def __init__(self, repository):
        self.repository = repository

    def create(self, routine_id, date, material, completed, summary):
        return self.repository.create(routine_id, date, material, completed, summary)

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, id):
        return self.repository.get_by_id(id)

    def delete(self, id):
        return self.repository.delete(id)

    def update(self, id, routine_id, date, material, completed, summary):
        return self.repository.update(id, routine_id, date, material, completed, summary)
