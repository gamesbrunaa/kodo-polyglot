from app.services.language_services import LanguageService


class FakeRepository:
    def get_all(self):
        return [
            {"id": 1, "name": "Français", "level": "A2"},
            {"id": 2, "name": "English", "level": "B1"},
        ]

    def create(self, name, level):
        return {"id": 1, "name": name, "level": level}

    def get_by_id(self, id):
        return {"id": id, "name": "Francês", "level": "A1"}

    def delete(self, id):
        return True

    def update(self, id, name, level):
        return {"id": id, "name": name, "level": level}


def test_get_all_returns_all_languages():
    repository = FakeRepository()
    service = LanguageService(repository)
    result = service.get_all()
    assert len(result) == 2


def test_create_language():
    repository = FakeRepository()
    service = LanguageService(repository)
    result = service.create("Espanhol", "A1")
    assert result["name"] == "Espanhol"
    assert result["level"] == "A1"


def test_get_by_id_returns_language():
    repository = FakeRepository()
    service = LanguageService(repository)
    result = service.get_by_id(1)
    assert result["id"] == 1
    assert result["name"] == "Francês"


def test_delete_language():
    repository = FakeRepository()
    service = LanguageService(repository)
    result = service.delete(1)
    assert result


def test_update_language():
    repository = FakeRepository()
    service = LanguageService(repository)
    result = service.update(1, "Français", "B1")
    assert result["name"] == "Français"
    assert result["level"] == "B1"
