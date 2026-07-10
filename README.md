# 🌍 kōdo-polyglot

A personal API for managing language study routines: track what you study, when, and how you're progressing.

Built with FastAPI, SQLAlchemy and MySQL.

---

## 💡 Why this project?

I study French and English daily and needed a way to organize my routine by skill (reading, writing, speaking, listening), track materials for each session, and see my progress over time. Instead of using a generic app, I build my own.

---

## Current status

** v1 - In Progress **
- [x] Project structure (FastAPI template)
- [x] Database models (Language, skill, routine, studySession)
- [x] Database connection (SQLAlchemy + MySQL)
- [ ] API endpoints (CRUD)
- [ ] Data validation (Pydantic schemas)
- [ ] Business logic (services)
- [ ] Unit tests

**Planned for v2:** vocabulary tracker (word, translation, context), study streak, statistics.

---

## 📂 Project structure
 
```
kodo-polyglot/
│
├── app/
│   ├── main.py                  # Entry point, starts the FastAPI server
│   ├── core/                    # Settings and database connection
│   ├── routes/                  # API endpoints
│   ├── schemas/                 # Request/response data validation
│   ├── services/                # Business logic
│   ├── repositories/            # Database models and queries
│   ├── adapters/                # External integrations
│   └── utils/                   # Helper functions
│
├── tests/                       # Unit tests (pytest)
├── .env.example                 # Environment variables template
├── Dockerfile                   # Container image
├── docker-compose.yml           # App + MySQL containers
└── pyproject.toml               # Dependencies & tool settings
```
 
---
 
## Data model
 
```
┌──────────────┐     ┌──────────────┐
│   Language   │     │    Skill     │
│──────────────│     │──────────────│
│ id           │     │ id           │
│ name         │     │ name         │
│ level        │     │              │
└──────┬───────┘     └──────┬───────┘
       │                    │
       └────────┬───────────┘
                │
         ┌──────┴───────┐
         │   Routine    │
         │──────────────│
         │ id           │
         │ day_of_week  │
         │ language_id  │
         │ skill_id     │
         └──────┬───────┘
                │
        ┌───────┴────────┐
        │ Study Session  │
        │────────────────│
        │ id             │
        │ routine_id     │
        │ date           │
        │ material       │
        │ completed      │
        │ summary        │
        └────────────────┘
```
 
---

## 🛠️ Tech stack
 
- **Python 3.11+**
- **FastAPI** + **Uvicorn**
- **MySQL** + **SQLAlchemy**
- **Docker** + **Docker Compose**
- **Pytest** for testing
- **Ruff** for linting & formatting
---
 
## 🚀 Getting started
 
### 1. Clone and setup
 
```bash
git clone https://github.com/gamesbrunaa/kodo-polyglot.git
cd kodo-polyglot
python3 -m venv .venv
. .venv/bin/activate
pip install -e .[dev]
```
 
### 2. Configure environment
 
```bash
cp .env.example .env
# Edit .env with your database credentials
```
 
### 3. Create the database
 
```bash
mysql -u root -p -e "CREATE DATABASE kodo_polyglot;"
```
 
### 4. Run
 
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
 
API docs available at `http://localhost:8000/docs`
 
---
 
## 🧪 Quality
 
| Tool | Command | What it does |
|---|---|---|
| **Ruff** | `ruff check .` | Linting and code style |
| **Ruff** | `ruff format .` | Auto-format code |
| **Pytest** | `pytest` | Run tests |
| **MyPy** | `mypy app/` | Type checking |
 
---
 
## 📝 Commit Convention
 
This project follows [Conventional Commits](https://www.conventionalcommits.org/):
 
```
feat: add language CRUD endpoints
fix: correct foreign key in study session model
docs: update README with data model diagram
```
 
---
 
## 📄 License
 
MIT