from fastapi import APIRouter, Depends

from app.core.database import SessionLocal
from app.repositories.language_repository import LanguageRepository
from app.schemas.language_schemas import LanguageCreate, LanguageResponse
from app.services.language_services import LanguageService

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/languages", response_model=LanguageResponse)
def create_language(language: LanguageCreate, db=Depends(get_db)):
    service = LanguageService(LanguageRepository(db))
    return service.create(language.name, language.level)


@router.get("/languages", response_model=list[LanguageResponse])
def get_languages(db=Depends(get_db)):
    service = LanguageService(LanguageRepository(db))
    return service.get_all()


@router.delete("/languages/{language_id}")
def delete_language(language_id: int, db=Depends(get_db)):
    service = LanguageService(LanguageRepository(db))
    return service.delete(language_id)


@router.put("/languages/{language_id}", response_model=LanguageResponse)
def update_language(language_id: int, data: LanguageCreate, db=Depends(get_db)):
    service = LanguageService(LanguageRepository(db))
    return service.update(language_id, data.name, data.level)
