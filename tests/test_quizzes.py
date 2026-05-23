"""Integration tests for the /quizzes API endpoints."""


def test_create_quiz(client, SAMPLE_QUIZ):
    r = client.post("/quizzes/", json=SAMPLE_QUIZ)
    assert r.status_code == 201
    body = r.json()
    assert body["title"] == SAMPLE_QUIZ["title"]
    assert "id" in body
    assert len(body["questions"]) == 1


def test_list_quizzes_empty(client):
    r = client.get("/quizzes/")
    assert r.status_code == 200
    assert r.json() == []


def test_list_quizzes_filter_by_topic(client, SAMPLE_QUIZ):
    client.post("/quizzes/", json=SAMPLE_QUIZ)
    other = {**SAMPLE_QUIZ, "topic": "Math", "title": "Geometry Quiz"}
    client.post("/quizzes/", json=other)

    r = client.get("/quizzes/?topic=Python")
    assert len(r.json()) == 1


def test_list_quizzes_filter_by_difficulty(client, SAMPLE_QUIZ):
    client.post("/quizzes/", json=SAMPLE_QUIZ)
    hard = {**SAMPLE_QUIZ, "title": "Advanced Python", "difficulty": 5}
    client.post("/quizzes/", json=hard)

    r = client.get("/quizzes/?difficulty=5")
    results = r.json()
    assert len(results) == 1
    assert results[0]["difficulty"] == 5


def test_get_quiz_not_found(client):
    r = client.get("/quizzes/999")
    assert r.status_code == 404


def test_get_quiz_by_id(client, SAMPLE_QUIZ):
    created = client.post("/quizzes/", json=SAMPLE_QUIZ).json()
    r = client.get(f"/quizzes/{created['id']}")
    assert r.status_code == 200
    assert r.json()["id"] == created["id"]


def test_update_quiz_title(client, SAMPLE_QUIZ):
    created = client.post("/quizzes/", json=SAMPLE_QUIZ).json()
    r = client.patch(f"/quizzes/{created['id']}", json={"title": "Updated Title"})
    assert r.status_code == 200
    assert r.json()["title"] == "Updated Title"


def test_update_quiz_not_found(client):
    r = client.patch("/quizzes/999", json={"title": "X"})
    assert r.status_code == 404


def test_delete_quiz(client, SAMPLE_QUIZ):
    created = client.post("/quizzes/", json=SAMPLE_QUIZ).json()
    r = client.delete(f"/quizzes/{created['id']}")
    assert r.status_code == 204
    assert client.get(f"/quizzes/{created['id']}").status_code == 404


def test_delete_quiz_not_found(client):
    r = client.delete("/quizzes/999")
    assert r.status_code == 404
