from fastapi import FastAPI

from app.core.database import Base, engine
from app.routes.language_routes import router as language_router
from app.routes.routine_routes import routes as routine_router
from app.routes.skill_routes import router as skill_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="kōdo-polyglot", description="Language study routine tracker")

app.include_router(language_router)
app.include_router(skill_router)
app.include_router(routine_router)
