from fastapi import APIRouter, Depends

from app.core.database import SessionLocal
from app.repositories.study_sessions_repository import StudySessionRepository
from app.schemas.study_session_schemas import StudySessionCreate, StudySessionResponse
from app.services.study_session_services import StudySessionService

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/studysessions", response_model=StudySessionResponse)
def create_study_session(study_session: StudySessionCreate, db=Depends(get_db)):
    service = StudySessionService(StudySessionRepository(db))
    return service.create(
        study_session.routine_id,
        study_session.date,
        study_session.material,
        study_session.completed,
        study_session.summary,
    )


@router.get("/studysessions", response_model=list[StudySessionResponse])
def get_study_sessions(db=Depends(get_db)):
    service = StudySessionService(StudySessionRepository(db))
    return service.get_all()


@router.delete("/studysessions/{study_session_id}")
def delete_study_sessions(study_session_id: int, db=Depends(get_db)):
    service = StudySessionService(StudySessionRepository(db))
    return service.delete(study_session_id)


@router.put("/studysessions/{study_session_id}", response_model=StudySessionResponse)
def update_study_session(study_session_id: int, data: StudySessionCreate, db=Depends(get_db)):
    service = StudySessionService(StudySessionRepository(db))
    return service.update(study_session_id, data.routine_id, data.date, data.material, data.completed, data.summary)
