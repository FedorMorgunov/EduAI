# EduAI — AI-powered Educational Platform

EduAI is a RESTful backend service that generates adaptive quizzes and delivers structured lessons powered by AI. Built with Python and FastAPI.

## Features

- Adaptive quiz generation per topic and difficulty
- Structured lesson catalogue with content management
- Health-check and readiness endpoints
- Fully tested with pytest (unit, integration, API tests)
- Static analysis enforced via flake8
- CI/CD via GitHub Actions

## Tech Stack

| Layer      | Technology              |
|------------|-------------------------|
| Language   | Python 3.11             |
| Framework  | FastAPI                 |
| Testing    | pytest + httpx          |
| Linting    | flake8                  |
| CI/CD      | GitHub Actions          |

## Quick Start

```bash
# 1. Clone and enter the repo
git clone https://github.com/FedorMorgunov/EduAI.git
cd EduAI

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# 4. Run the server
uvicorn app.main:app --reload

# 5. Open interactive docs
open http://localhost:8000/docs
```

## Running Tests

```bash
pytest tests/ -v --tb=short
```

## Linting

```bash
flake8 app/ tests/
```

## Project Structure

```
EduAI/
├── app/
│   ├── main.py          # FastAPI application entry point
│   ├── routes/          # Route handlers
│   ├── models/          # Pydantic data models
│   └── services/        # Business logic
├── tests/               # pytest test suite
├── docs/                # Extra documentation
│   ├── git-flow.md      # Branching & commit conventions
│   └── test-report.md   # Manual test report
├── .github/workflows/   # CI/CD pipelines
├── .flake8              # Linter configuration
├── .gitignore
├── requirements.txt
└── requirements-dev.txt
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for branch naming, commit conventions, and the PR process.

## License

[MIT](LICENSE)
