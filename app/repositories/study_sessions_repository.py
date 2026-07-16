from app.repositories.study_sessions_models import StudySession


class StudySessionRepository:
    def __init__(self, db):
        self.db = db

    def create(self, routine_id, date, material, completed, summary):
        new_study_session = StudySession(
            routine_id=routine_id, date=date, material=material, completed=completed, summary=summary
        )
        self.db.add(new_study_session)
        self.db.commit()
        self.db.refresh(new_study_session)
        return new_study_session

    def get_all(self):
        return self.db.query(StudySession).all()

    def get_by_id(self, id):
        return self.db.query(StudySession).filter(StudySession.id == id).first()

    def delete(self, id):
        study_session = self.get_by_id(id)
        self.db.delete(study_session)
        self.db.commit()
        return True

    def update(self, id, routine_id, date, material, completed, summary):
        study_session = self.get_by_id(id)
        study_session.routine_id = routine_id
        study_session.date = date
        study_session.material = material
        study_session.completed = completed
        study_session.summary = summary
        self.db.commit()
        self.db.refresh(study_session)
        return study_session
