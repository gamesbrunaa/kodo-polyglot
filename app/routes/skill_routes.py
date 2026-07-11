from fastapi import APIRouter, Depends

from app.core.database import SessionLocal
from app.repositories.skills_model import Skills
from app.schemas.skill_schemas import SkillCreate, SkillResponse

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/skills", response_model=SkillResponse)
def create_skill(skill: SkillCreate, db=Depends(get_db)):
    new_skill = Skills(name=skill.name)
    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)
    return new_skill


@router.get("/skills", response_model=list[SkillResponse])
def get_skills(db=Depends(get_db)):
    skills = db.query(Skills).all()
    return skills


@router.delete("/skills/{skill_id}")
def delete_skill(skill_id: int, db=Depends(get_db)):
    skill = db.query(Skills).filter(Skills.id == skill_id).first()
    db.delete(skill)
    db.commit()
    return True


@router.put("/skills/{skill_id}", response_model=SkillResponse)
def update_skill(skill_id: int, data: SkillCreate, db=Depends(get_db)):
    skill = db.query(Skills).filter(Skills.id == skill_id).first()
    skill.name = data.name
    db.commit()
    db.refresh(skill)
    return skill
