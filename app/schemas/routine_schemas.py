from pydantic import BaseModel


class RoutineCreate(BaseModel):
    day_of_week: str
    language_id: int
    skill_id: int


class RoutineResponse(BaseModel):
    id: int
    day_of_week: str
    language_id: int
    skill_id: int
    model_config = {"from_attributes": True}
