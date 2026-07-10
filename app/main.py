from app.core.database import engine, Base
from app.repositories.language_model import Language
from app.repositories.routine_models import Routine
from app.repositories.skills_model import Skills
from app.repositories.study_sessions import StudySession

Base.metadata.create_all(bind=engine)

print("Tabelas criadas com sucesso!")
