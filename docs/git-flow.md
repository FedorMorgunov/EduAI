# Git Flow & Conventional Commits — Quick Reference

See full documentation in [CONTRIBUTING.md](../CONTRIBUTING.md).

## Branch Map

```
main ──────────────────────────────────────────────── (production)
  └─ develop ──────────────────────────────────────── (integration)
       ├─ feature/quiz-difficulty-filter
       ├─ fix/lesson-404-response
       ├─ chore/upgrade-fastapi
       └─ docs/update-readme
```

## Commit Cheatsheet

| Scenario | Commit message |
|---|---|
| New quiz filter | `feat(quiz): add difficulty filter to list endpoint` |
| Fix 404 bug | `fix(lesson): return 404 when lesson id not found` |
| Add tests | `test(quiz): add integration tests for CRUD` |
| CI tweak | `ci: cache pip dependencies in GitHub Actions` |
| Bump deps | `chore(deps): upgrade pydantic to 2.7.1` |
| Breaking change | `feat(auth)!: replace API keys with JWT` |

## Release Checklist

- [ ] All tests pass on `develop`
- [ ] PR from `develop` → `main` reviewed & merged
- [ ] Tag created: `git tag -a v0.x.y -m "Release v0.x.y"`
- [ ] Tag pushed: `git push origin v0.x.y`
- [ ] GitHub release published automatically by CI
