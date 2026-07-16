class RoutineService:
    def __init__(self, repository):
        self.repository = repository

    def create(self, day_of_week, language_id, skill_id):
        return self.repository.create(day_of_week, language_id, skill_id)

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, id):
        return self.repository.get_by_id(id)

    def delete(self, id):
        return self.repository.delete(id)

    def update(self, id, day_of_week, language_id, skill_id):
        return self.repository.update(id, day_of_week, language_id, skill_id)
