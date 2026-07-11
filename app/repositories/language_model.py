from sqlalchemy import Column, Integer, String

from app.core.database import Base


class Language(Base):
    __tablename__ = "languages"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    level = Column(String(255), nullable=False)
