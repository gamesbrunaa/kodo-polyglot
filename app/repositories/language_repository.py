from app.repositories.language_model import Language


class LanguageRepository:
    def __init__(self, db):
        self.db = db

    def create(self, name, level):
        new_language = Language(name=name, level=level)
        self.db.add(new_language)
        self.db.commit()
        self.db.refresh(new_language)
        return new_language

    def get_all(self):
        return self.db.query(Language).all()

    def get_by_id(self, id):
        return self.db.query(Language).filter(Language.id == id).first()

    def delete(self, id):
        language = self.get_by_id(id)
        self.db.delete(language)
        self.db.commit()
        return True

    def update(self, id, name, level):
        language = self.get_by_id(id)
        language.name = name
        language.level = level
        self.db.commit()
        self.db.refresh(language)
        return language
