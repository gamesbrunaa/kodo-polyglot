from app.repositories.routine_models import Routine


class RoutineRepository:
    def __init__(self, db):
        self.db = db

    def create(self, day_of_week, language_id, skill_id):
        new_routine = Routine(day_of_week=day_of_week, language_id=language_id, skill_id=skill_id)
        self.db.add(new_routine)
        self.db.commit()
        self.db.refresh(new_routine)
        return new_routine

    def get_all(self):
        return self.db.query(Routine).all()

    def get_by_id(self, id):
        return self.db.query(Routine).filter(Routine.id == id).first()

    def delete(self, id):
        routine = self.get_by_id(id)
        self.db.delete(routine)
        self.db.commit()
        return True

    def update(self, id, day_of_week, language_id, skill_id):
        routine = self.get_by_id(id)
        routine.day_of_week = day_of_week
        routine.language_id = language_id
        routine.skill_id = skill_id
        self.db.commit()
        self.db.refresh(routine)
        return routine
