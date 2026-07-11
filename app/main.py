from fastapi import FastAPI

from app.core.database import Base, engine
from app.routes.language_routes import router as language_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="kōdo-polyglot", description="Language study routine tracker")

app.include_router(language_router)
