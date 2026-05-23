# Contributing Guide — Git Flow & Conventional Commits

## Branch Strategy (Git Flow)

```
main          ← stable production releases only
  └─ develop  ← integration branch (default target for PRs)
       ├─ feature/<short-description>   new features
       ├─ fix/<short-description>       bug fixes
       ├─ chore/<short-description>     tooling / deps / config
       └─ docs/<short-description>      documentation only
```

### Rules

| Branch | Who merges | Direct push? |
|--------|-----------|--------------|
| `main` | Release manager via PR | ❌ protected |
| `develop` | Any team member via PR | ❌ protected |
| `feature/*` | Author | ✅ |
| `fix/*` | Author | ✅ |

## Conventional Commits

All commit messages **must** follow [Conventional Commits v1.0.0](https://www.conventionalcommits.org/).

```
<type>(<scope>): <short summary>

[optional body]

[optional footer(s)]
```

### Types

| Type | When to use |
|------|-------------|
| `feat` | New feature visible to users |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `style` | Formatting, no logic change |
| `refactor` | Code restructure, no behaviour change |
| `test` | Adding or fixing tests |
| `chore` | Build scripts, deps, CI config |
| `perf` | Performance improvement |
| `ci` | CI/CD pipeline changes |

### Examples

```
feat(quiz): add difficulty-level filter to GET /quizzes
fix(lesson): return 404 when lesson not found
test(quiz): add integration tests for quiz creation
chore(deps): upgrade fastapi to 0.111.0
ci: add flake8 step to GitHub Actions workflow
docs: update README quick-start section
```

### Breaking Changes

Append `!` after the type or add `BREAKING CHANGE:` footer:

```
feat(auth)!: replace API-key auth with JWT

BREAKING CHANGE: all existing API keys are invalidated.
```

## Pull Request Process

1. Create branch from `develop`: `git checkout -b feature/my-feature develop`
2. Commit using Conventional Commits (small, atomic commits preferred)
3. Push and open PR targeting `develop`
4. Pass all CI checks (lint + tests)
5. Request review from at least 1 team member
6. Squash-merge into `develop`

## Release Process

1. Merge `develop` → `main` via PR
2. Tag the merge commit: `git tag -a v<MAJOR>.<MINOR>.<PATCH> -m "Release v<...>"`
3. Push the tag: `git push origin v<...>`
4. GitHub Actions publishes release notes automatically

## Versioning

We follow [Semantic Versioning 2.0.0](https://semver.org/):

- **MAJOR** — breaking API change
- **MINOR** — new backwards-compatible feature
- **PATCH** — backwards-compatible bug fix
