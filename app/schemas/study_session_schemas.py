from datetime import date

from pydantic import BaseModel


class StudySessionCreate(BaseModel):
    routine_id: int
    date: date
    material: str
    completed: bool
    summary: str | None


class StudySessionResponse(BaseModel):
    id: int
    routine_id: int
    date: date
    material: str
    completed: bool
    summary: str | None
    model_config = {"from_attributes": True}
