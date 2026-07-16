from fastapi import APIRouter, Depends

from app.core.database import SessionLocal
from app.repositories.skills_repository import SkillRepository
from app.schemas.skill_schemas import SkillCreate, SkillResponse
from app.services.skills_services import SkillsService

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/skills", response_model=SkillResponse)
def create_skill(skill: SkillCreate, db=Depends(get_db)):
    service = SkillsService(SkillRepository(db))
    return service.create(skill.name)


@router.get("/skills", response_model=list[SkillResponse])
def get_skills(db=Depends(get_db)):
    service = SkillsService(SkillRepository(db))
    return service.get_all()


@router.delete("/skills/{skill_id}")
def delete_skill(skill_id: int, db=Depends(get_db)):
    service = SkillsService(SkillRepository(db))
    return service.delete(skill_id)


@router.put("/skills/{skill_id}", response_model=SkillResponse)
def update_skill(skill_id: int, data: SkillCreate, db=Depends(get_db)):
    service = SkillsService(SkillRepository(db))
    return service.update(skill_id, data.name)
