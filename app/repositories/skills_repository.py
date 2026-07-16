from app.repositories.skills_model import Skills


class SkillRepository:
    def __init__(self, db):
        self.db = db

    def create(self, name):
        new_skill = Skills(name=name)
        self.db.add(new_skill)
        self.db.commit()
        self.db.refresh(new_skill)
        return new_skill

    def get_all(self):
        return self.db.query(Skills).all()

    def get_by_id(self, id):
        return self.db.query(Skills).filter(Skills.id == id).first()

    def delete(self, id):
        skill = self.get_by_id(id)
        self.db.delete(skill)
        self.db.commit()
        return True

    def update(self, id, name):
        skill = self.get_by_id(id)
        skill.name = name
        self.db.commit()
        self.db.refresh(skill)
        return skill
