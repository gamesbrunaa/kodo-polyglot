from fastapi import APIRouter, Depends

from app.core.database import SessionLocal
from app.repositories.routine_models import Routine
from app.schemas.routine_schemas import RoutineCreate, RoutineResponse

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/routines", response_model=RoutineResponse)
def create_routine(routine: RoutineCreate, db=Depends(get_db)):
    new_routine = Routine(day_of_week=routine.day_of_week, language_id=routine.language_id, skill_id=routine.skill_id)
    db.add(new_routine)
    db.commit()
    db.refresh(new_routine)
    return new_routine


@router.get("/routines", response_model=list[RoutineResponse])
def get_routines(db=Depends(get_db)):
    routines = db.query(Routine).all()
    return routines


@router.delete("/routines/{routine_id}")
def delete_routine(routine_id: int, db=Depends(get_db)):
    routine = db.query(Routine).filter(Routine.id == routine_id).first()
    db.delete(routine)
    db.commit()
    return True


@router.put("/routines/{routine_id}", response_model=RoutineResponse)
def update_routine(routine_id: int, data: RoutineCreate, db=Depends(get_db)):
    routine = db.query(Routine).filter(Routine.id == routine_id).first()
    routine.day_of_week = data.day_of_week
    routine.language_id = data.language_id
    routine.skill_id = data.skill_id
    db.commit()
    db.refresh(routine)
    return routine
