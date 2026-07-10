from app.core.database import Base
from sqlalchemy import Column, Integer, String


class Skills(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
