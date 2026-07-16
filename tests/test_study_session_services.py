from app.services.study_session_services import StudySessionService


class FakeRepository:
    def get_all(self):
        return [
            {
                "id": 1,
                "routine_id": 1,
                "date": "2026-07-14",
                "material": "teste",
                "completed": True,
                "summary": "teste",
            },
            {
                "id": 2,
                "routine_id": 2,
                "date": "2026-07-14",
                "material": "teste",
                "completed": True,
                "summary": "teste",
            },
        ]

    def create(self, routine_id, date, material, completed, summary):
        return {
            "id": 1,
            "routine_id": routine_id,
            "date": date,
            "material": material,
            "completed": completed,
            "summary": summary,
        }

    def get_by_id(self, id):
        return {
            "id": id,
            "routine_id": 1,
            "date": "2026-07-14",
            "material": "teste",
            "completed": True,
            "summary": "teste",
        }

    def delete(self, id):
        return True

    def update(self, id, routine_id, date, material, completed, summary):
        return {
            "id": id,
            "routine_id": routine_id,
            "date": date,
            "material": material,
            "completed": completed,
            "summary": summary,
        }


def test_get_all_returns_all_study_session():
    repository = FakeRepository()
    service = StudySessionService(repository)
    result = service.get_all()
    assert len(result) == 2


def test_create_study_session():
    repository = FakeRepository()
    service = StudySessionService(repository)
    result = service.create(1, "2026-07-14", "teste2", False, "teste22")
    assert result["routine_id"] == 1
    assert result["date"] == "2026-07-14"
    assert result["material"] == "teste2"
    assert not result["completed"]
    assert result["summary"] == "teste22"


def test_get_by_id_returns_study_session():
    repository = FakeRepository()
    service = StudySessionService(repository)
    result = service.get_by_id(1)
    assert result["id"] == 1
    assert result["routine_id"] == 1
    assert result["date"] == "2026-07-14"
    assert result["material"] == "teste"
    assert result["completed"]
    assert result["summary"] == "teste"


def test_delete_study_session():
    repository = FakeRepository()
    service = StudySessionService(repository)
    result = service.delete(1)
    assert result


def test_update_study_session():
    repository = FakeRepository()
    service = StudySessionService(repository)
    result = service.update(1, 1, "2026-07-14", "teste", False, "teste")
    assert result["routine_id"] == 1
    assert result["date"] == "2026-07-14"
    assert result["material"] == "teste"
    assert not result["completed"]
    assert result["summary"] == "teste"
