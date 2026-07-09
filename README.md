# ⚡ Python FastAPI Template

Personal template for building RESTful APIs with FastAPI.  
Endpoints, data validation, database integration.

---

## 📂 Project Structure

```
python-fastapi-template/
│
├── app/
│   ├── main.py                # Entry point
│   │
│   ├── core/                  # Settings, database connection, logger
│   │   └── __init__.py
│   │
│   ├── routes/                # API endpoints
│   │   └── __init__.py
│   │
│   ├── schemas/               # Request/response data validation
│   │   └── __init__.py
│   │
│   ├── services/              # Business logic
│   │   └── __init__.py
│   │
│   ├── repositories/          # Database access layer (queries and models)
│   │   └── __init__.py
│   │
│   ├── adapters/              # External integrations (APIs, email, etc.)
│   │   └── __init__.py
│   │
│   └── utils/                 # Helper functions (dates, strings, formatting)
│       └── __init__.py
│
├── tests/                     # Unit tests (pytest)
│   └── __init__.py
│
├── .env.example               # Environment variables template
├── .gitignore                 # Files excluded from version control
├── pyproject.toml             # Dependencies and tool settings
├── Dockerfile                 # Container image for the app
├── docker-compose.yml         # Container setup (app + MySQL)
└── README.md
```

---

## 🏗️ Architecture

Each folder has a clear responsibility:

| Folder | What it does | Example |
|---|---|---|
| `core/` | Centralized settings and connections | Database config, environment variables, logger |
| `routes/` | API endpoints — receives and responds to HTTP requests | `GET /users`, `POST /reports` |
| `schemas/` | Validates incoming data and defines response format | Required fields, data types, error messages |
| `services/` | Business logic and data processing | Generate reports, classify tickets, transform data |
| `repositories/` | Talks to the database — and nothing else | Queries, SQLAlchemy models |
| `adapters/` | Connects to external services | Zendesk API, email (SMTP), OpenAI |
| `utils/` | Generic reusable helpers | Date formatting, string manipulation |

> **Request flow:** route receives → schema validates → service processes → repository fetches/saves → response returns.

---

## 🚀 Getting Started

### 1. Clone and setup

```bash
git clone https://github.com/gamesbrunaa/python-fastapi-template.git
cd python-fastapi-template
python -m venv .venv
. .venv/bin/activate
pip install -e .[dev]
```

### 2. Configure environment

```bash
cp .env.example .env
# Edit .env with your credentials
```

### 3. Run

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at `http://localhost:8000`  
Interactive docs (Swagger) at `http://localhost:8000/docs`

### 4. Run with Docker

```bash
cp .env.example .env
docker compose up -d
```

---

## 🧪 Quality

| Tool | Command | What it does |
|---|---|---|
| **Ruff** | `ruff check .` | Linting and code style |
| **Ruff** | `ruff format .` | Auto-format code |
| **Pytest** | `pytest` | Run tests |
| **MyPy** | `mypy app/` | Type checking |
| **Docker** | `docker compose up -d` | Start containers |

---

## 📝 Commit Convention

This project follows [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add user registration endpoint
fix: correct validation on email schema
chore: update dependencies
docs: add API examples to README
```

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **FastAPI** + **Uvicorn**
- **MySQL** + **SQLAlchemy**
- **Docker** + **Docker Compose**
- **Pytest** for testing
- **Ruff** for linting & formatting

---

## 📄 License

MIT