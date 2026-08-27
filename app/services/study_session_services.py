class StudySessionService:
    def __init__(self, repository, routine_repository=None):
        self.repository = repository
        self.routine_repository = routine_repository

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

    def generate_daily_sessions(self, day_of_week, date):
        routines = self.routine_repository.get_by_day(day_of_week)
        created = []

        for routine in routines:
            existing = self.repository.get_by_routine_and_date(routine.id, date)
            if not existing:
                session = self.repository.create(
                    routine_id=routine.id, date=date, material="", completed=False, summary=None
                )
                created.append(session)

        return created
