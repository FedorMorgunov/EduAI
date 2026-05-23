# Changelog

All notable changes to EduAI are documented here.  
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);  
versioning follows [Semantic Versioning](https://semver.org/).

---

## [v0.1.0] — 2026-05-23

### Added
- **GET/POST/PATCH/DELETE /lessons** — full CRUD API for lesson content with topic filtering
- **GET/POST/PATCH/DELETE /quizzes** — full CRUD API for adaptive quizzes with topic + difficulty filtering
- **GET /health** — service health-check endpoint (returns version, status)
- **33 automated tests** across 4 test files (unit · integration · API) — all green
- **flake8** static analysis enforced in CI; zero violations at release
- **GitHub Actions CI pipeline**: lint (flake8) → test (pytest) → GitHub Release on tag push
- **CONTRIBUTING.md** with Git Flow branching strategy and Conventional Commits specification
- **docs/git-flow.md** — branch map and commit message cheatsheet
- **docs/test-report.md** — manual test report (5 scenarios, all PASS)
- **README.md** with quick-start, project structure, and contribution guide
- **requirements.txt** / **requirements-dev.txt** — pinned dependencies
- **.gitignore** — Python, IDE, venv, coverage artefacts

### Architecture
- FastAPI 0.111 + Pydantic v2 + uvicorn
- In-memory service layer (stateless, easily replaced by a database)
- pytest + httpx for synchronous API-level testing

---

[v0.1.0]: https://github.com/FedorMorgunov/EduAI/releases/tag/v0.1.0
