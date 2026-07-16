from app.services.skills_services import SkillsService


class FakeRepository:
    def get_all(self):
        return [
            {"id": 1, "name": "Leitura"},
            {"id": 2, "name": "Speaking"},
        ]

    def create(self, name):
        return {"id": 1, "name": name}

    def get_by_id(self, id):
        return {"id": id, "name": "Reading"}

    def delete(self, id):
        return True

    def update(self, id, name):
        return {"id": id, "name": name}


def test_get_all_returns_all_skill():
    repository = FakeRepository()
    service = SkillsService(repository)
    result = service.get_all()
    assert len(result) == 2


def test_create_skill():
    repository = FakeRepository()
    service = SkillsService(repository)
    result = service.create("Writing")
    assert result["name"] == "Writing"


def test_get_by_id_returns_skill():
    repository = FakeRepository()
    service = SkillsService(repository)
    result = service.get_by_id(1)
    assert result["id"] == 1
    assert result["name"] == "Reading"


def test_delete_skill():
    repository = FakeRepository()
    service = SkillsService(repository)
    result = service.delete(1)
    assert result


def test_update_skill():
    repository = FakeRepository()
    service = SkillsService(repository)
    result = service.update(1, "Listening")
    assert result["name"] == "Listening"
