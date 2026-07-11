from pydantic import BaseModel


class LanguageCreate(BaseModel):
    name: str
    level: str | None = None


class LanguageResponse(BaseModel):
    id: int
    name: str
    level: str | None = None
    model_config = {"from_attributes": True}
