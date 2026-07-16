class SkillsService:
    def __init__(self, repository):
        self.repository = repository

    def create(self, name):
        return self.repository.create(name)

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, id):
        return self.repository.get_by_id(id)

    def delete(self, id):
        return self.repository.delete(id)

    def update(self, id, name):
        return self.repository.update(id, name)
