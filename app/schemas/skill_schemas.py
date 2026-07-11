from pydantic import BaseModel


class SkillCreate(BaseModel):
    name: str


class SkillResponse(BaseModel):
    id: int
    name: str
    model_config = {"from_attributes": True}
