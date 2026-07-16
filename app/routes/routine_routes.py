from fastapi import APIRouter, Depends

from app.core.database import SessionLocal
from app.repositories.routine_repository import RoutineRepository
from app.schemas.routine_schemas import RoutineCreate, RoutineResponse
from app.services.routine_services import RoutineService

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/routines", response_model=RoutineResponse)
def create_routine(routine: RoutineCreate, db=Depends(get_db)):
    service = RoutineService(RoutineRepository(db))
    return service.create(routine.day_of_week, routine.language_id, routine.skill_id)


@router.get("/routines", response_model=list[RoutineResponse])
def get_routines(db=Depends(get_db)):
    service = RoutineService(RoutineRepository(db))
    return service.get_all()


@router.delete("/routines/{routine_id}")
def delete_routine(routine_id: int, db=Depends(get_db)):
    service = RoutineService(RoutineRepository(db))
    return service.delete(routine_id)


@router.put("/routines/{routine_id}", response_model=RoutineResponse)
def update_routine(routine_id: int, data: RoutineCreate, db=Depends(get_db)):
    service = RoutineService(RoutineRepository(db))
    return service.update(routine_id, data.day_of_week, data.language_id, data.skill_id)
