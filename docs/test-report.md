# Manual Test Report — EduAI v0.1.0

**Date:** 2026-05-23  
**Tester:** Fedor Morgunov  
**Environment:** Local — `uvicorn app.main:app --reload` on `http://localhost:8000`  
**Tool:** curl + Swagger UI (`/docs`)

---

## Test Scenario 1 — Health Check

**Objective:** Verify the service starts and returns a healthy status.

**Steps:**
1. Start the server: `uvicorn app.main:app --reload`
2. Send `GET http://localhost:8000/health`

**Expected result:** HTTP 200, body `{"status":"ok","service":"EduAI","version":"0.1.0"}`

**Actual result:**
```json
HTTP/1.1 200 OK
{"status": "ok", "service": "EduAI", "version": "0.1.0"}
```

**Status:** ✅ PASS

---

## Test Scenario 2 — Create and Retrieve a Lesson

**Objective:** Confirm lesson creation stores data and GET returns it correctly.

**Steps:**
1. `POST /lessons/` with body:
```json
{
  "title": "Introduction to Python",
  "topic": "Python",
  "content": "Python is a high-level language.",
  "difficulty": 1
}
```
2. Note the returned `id`.
3. `GET /lessons/{id}`

**Expected result:**
- POST → HTTP 201, response contains `id`, `title`, `topic`
- GET → HTTP 200, same data as created

**Actual result:**
- POST → `201 Created`, `{"id":1,"title":"Introduction to Python",...}`
- GET → `200 OK`, identical payload

**Status:** ✅ PASS

---

## Test Scenario 3 — Filter Lessons by Topic

**Objective:** Verify topic query-param filter returns only matching lessons.

**Steps:**
1. Create lesson with `topic: "Python"`
2. Create lesson with `topic: "Math"`
3. `GET /lessons/?topic=Python`

**Expected result:** Array with exactly 1 item, `topic == "Python"`

**Actual result:**
```json
[{"id":1,"title":"Introduction to Python","topic":"Python","difficulty":1,...}]
```

**Status:** ✅ PASS

---

## Test Scenario 4 — Create Quiz and Filter by Difficulty

**Objective:** Confirm quiz creation and difficulty-based filtering work end-to-end.

**Steps:**
1. `POST /quizzes/` with difficulty 1
2. `POST /quizzes/` with difficulty 5
3. `GET /quizzes/?difficulty=5`

**Expected result:** Exactly 1 quiz with `difficulty == 5`

**Actual result:**
```json
[{"id":2,"title":"Advanced Python","difficulty":5,...}]
```

**Status:** ✅ PASS

---

## Test Scenario 5 — Update and Delete a Lesson

**Objective:** PATCH updates a field; DELETE removes the resource; subsequent GET returns 404.

**Steps:**
1. `POST /lessons/` → note `id`
2. `PATCH /lessons/{id}` with `{"difficulty": 4}`
3. `GET /lessons/{id}` — confirm difficulty updated
4. `DELETE /lessons/{id}`
5. `GET /lessons/{id}` — confirm 404

**Expected result:** Steps 2–3 show `difficulty: 4`; step 5 returns HTTP 404.

**Actual result:**
- PATCH → `200 OK`, `"difficulty": 4`
- GET after PATCH → `200 OK`, `"difficulty": 4`
- DELETE → `204 No Content`
- GET after DELETE → `404 Not Found`

**Status:** ✅ PASS

---

## Summary

| # | Scenario | Result |
|---|----------|--------|
| 1 | Health check | ✅ PASS |
| 2 | Create & retrieve lesson | ✅ PASS |
| 3 | Filter lessons by topic | ✅ PASS |
| 4 | Create quiz & filter by difficulty | ✅ PASS |
| 5 | Update & delete lesson | ✅ PASS |

**All 5 scenarios passed. No defects found.**
