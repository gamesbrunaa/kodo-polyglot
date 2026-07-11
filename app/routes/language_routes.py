from fastapi import APIRouter, Depends

from app.core.database import SessionLocal
from app.repositories.language_model import Language
from app.schemas.language_schemas import LanguageCreate, LanguageResponse

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/languages", response_model=LanguageResponse)
def create_language(language: LanguageCreate, db=Depends(get_db)):
    new_language = Language(name=language.name, level=language.level)
    db.add(new_language)
    db.commit()
    db.refresh(new_language)
    return new_language


@router.get("/languages", response_model=list[LanguageResponse])
def get_languages(db=Depends(get_db)):
    languages = db.query(Language).all()
    return languages


@router.delete("/languages/{language_id}")
def delete_language(language_id: int, db=Depends(get_db)):
    language = db.query(Language).filter(Language.id == language_id).first()
    db.delete(language)
    db.commit()
    return True


@router.put("/languages/{language_id}", response_model=LanguageResponse)
def update_language(language_id: int, data: LanguageCreate, db=Depends(get_db)):
    language = db.query(Language).filter(Language.id == language_id).first()
    language.name = data.name
    language.level = data.level
    db.commit()
    db.refresh(language)
    return language
