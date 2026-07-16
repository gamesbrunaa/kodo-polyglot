from app.services.routine_services import RoutineService


class FakeRepository:
    def get_all(self):
        return [
            {"id": 1, "day_of_week": "Segunda", "language_id": 1, "skill_id": 2},
            {"id": 2, "day_of_week": "Terça", "language_id": 2, "skill_id": 2},
        ]

    def create(self, day_of_week, language_id, skill_id):
        return {"id": 1, "day_of_week": day_of_week, "language_id": language_id, "skill_id": skill_id}

    def get_by_id(self, id):
        return {"id": id, "day_of_week": "Quarta", "language_id": 1, "skill_id": 2}

    def delete(self, id):
        return True

    def update(self, id, day_of_week, language_id, skill_id):
        return {"id": 1, "day_of_week": "Quinta", "language_id": 1, "skill_id": 2}


def test_get_all_returns_all_routine():
    repository = FakeRepository()
    service = RoutineService(repository)
    result = service.get_all()
    assert len(result) == 2


def test_create_routine():
    repository = FakeRepository()
    service = RoutineService(repository)
    result = service.create("Segunda", 1, 1)
    assert result["day_of_week"] == "Segunda"
    assert result["language_id"] == 1
    assert result["skill_id"] == 1


def test_get_by_id_returns_routine():
    repository = FakeRepository()
    service = RoutineService(repository)
    result = service.get_by_id(1)
    assert result["id"] == 1
    assert result["day_of_week"] == "Quarta"
    assert result["language_id"] == 1
    assert result["skill_id"] == 2


def test_delete_routine():
    repository = FakeRepository()
    service = RoutineService(repository)
    result = service.delete(1)
    assert result


def test_update_routine():
    repository = FakeRepository()
    service = RoutineService(repository)
    result = service.update(1, "Quinta", 1, 2)
    assert result["day_of_week"] == "Quinta"
    assert result["language_id"] == 1
    assert result["skill_id"] == 2
