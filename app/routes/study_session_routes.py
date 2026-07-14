from fastapi import APIRouter, Depends

from app.core.database import SessionLocal
from app.repositories.study_sessions_models import StudySession
from app.schemas.study_session_schemas import StudySessionCreate, StudySessionResponse

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/studysessions", response_model=StudySessionResponse)
def create_study_session(study_session: StudySessionCreate, db=Depends(get_db)):
    new_study_session = StudySession(
        routine_id=study_session.routine_id,
        date=study_session.date,
        material=study_session.material,
        completed=study_session.completed,
        summary=study_session.summary,
    )
    db.add(new_study_session)
    db.commit()
    db.refresh(new_study_session)
    return new_study_session


@router.get("/studysessions", response_model=list[StudySessionResponse])
def get_study_sessions(db=Depends(get_db)):
    study_sessions = db.query(StudySession).all()
    return study_sessions


@router.delete("/studysessions/{study_sessions_id}")
def delete_study_sessions(study_session_id: int, db=Depends(get_db)):
    study_session = db.query(StudySession).filter(StudySession.id == study_session_id).first()
    db.delete(study_session)
    db.commit()
    return True


@router.put("/studysessions/{study_sessions_id}", response_model=StudySessionResponse)
def update_study_session(study_session_id: int, data: StudySessionCreate, db=Depends(get_db)):
    study_session = db.query(StudySession).filter(StudySession.id == study_session_id).first()
    study_session.routine_id = data.routine_id
    study_session.date = data.date
    study_session.material = data.material
    study_session.completed = data.completed
    study_session.summary = data.summary
    db.commit()
    db.refresh(study_session)
    return study_session
