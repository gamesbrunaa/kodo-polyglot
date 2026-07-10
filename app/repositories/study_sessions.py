from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String

from app.core.database import Base


class StudySession(Base):
    __tablename__ = "study_sessions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    routine_id = Column(Integer, ForeignKey("routine.id"), nullable=False)
    date = Column(Date, nullable=False)
    material = Column(String(255), nullable=False)
    completed = Column(Boolean, nullable=False)
    summary = Column(String(1024), nullable=True)
