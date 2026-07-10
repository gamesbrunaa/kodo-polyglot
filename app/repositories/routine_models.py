from sqlalchemy import Column, ForeignKey, Integer, String

from app.core.database import Base


class Routine(Base):
    __tablename__ = "routine"

    id = Column(Integer, primary_key=True, autoincrement=True)
    day_of_week = Column(String(50), nullable=False)
    language_id = Column(Integer, ForeignKey("languages.id"), nullable=False)
    skill_id = Column(Integer, ForeignKey("skills.id"), nullable=False)
