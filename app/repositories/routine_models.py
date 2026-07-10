from app.core.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Routine(Base):
    __tablename__ = "routine"

    id = Column(Integer, primary_key=True, autoincrement=True)
    day_of_week = Column(String(50), nullable=False)
    language_id = Column(Integer, ForeignKey("languages.id"), nullable=False)
    skill_id = Column(Integer, ForeignKey("skills.id"), nullable=False)
