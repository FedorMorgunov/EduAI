"""Integration tests for the /lessons API endpoints."""


def test_create_lesson(client, SAMPLE_LESSON):
    r = client.post("/lessons/", json=SAMPLE_LESSON)
    assert r.status_code == 201
    body = r.json()
    assert body["title"] == SAMPLE_LESSON["title"]
    assert body["topic"] == SAMPLE_LESSON["topic"]
    assert "id" in body


def test_list_lessons_empty(client):
    r = client.get("/lessons/")
    assert r.status_code == 200
    assert r.json() == []


def test_list_lessons_after_create(client, SAMPLE_LESSON):
    client.post("/lessons/", json=SAMPLE_LESSON)
    r = client.get("/lessons/")
    assert r.status_code == 200
    assert len(r.json()) == 1


def test_list_lessons_filter_by_topic(client, SAMPLE_LESSON):
    client.post("/lessons/", json=SAMPLE_LESSON)
    other = {**SAMPLE_LESSON, "topic": "Math", "title": "Algebra 101"}
    client.post("/lessons/", json=other)

    r = client.get("/lessons/?topic=Python")
    assert r.status_code == 200
    results = r.json()
    assert len(results) == 1
    assert results[0]["topic"] == "Python"


def test_get_lesson_not_found(client):
    r = client.get("/lessons/999")
    assert r.status_code == 404


def test_get_lesson_by_id(client, SAMPLE_LESSON):
    created = client.post("/lessons/", json=SAMPLE_LESSON).json()
    r = client.get(f"/lessons/{created['id']}")
    assert r.status_code == 200
    assert r.json()["id"] == created["id"]


def test_update_lesson(client, SAMPLE_LESSON):
    created = client.post("/lessons/", json=SAMPLE_LESSON).json()
    r = client.patch(f"/lessons/{created['id']}", json={"difficulty": 3})
    assert r.status_code == 200
    assert r.json()["difficulty"] == 3


def test_update_lesson_not_found(client):
    r = client.patch("/lessons/999", json={"difficulty": 2})
    assert r.status_code == 404


def test_delete_lesson(client, SAMPLE_LESSON):
    created = client.post("/lessons/", json=SAMPLE_LESSON).json()
    r = client.delete(f"/lessons/{created['id']}")
    assert r.status_code == 204
    assert client.get(f"/lessons/{created['id']}").status_code == 404


def test_delete_lesson_not_found(client):
    r = client.delete("/lessons/999")
    assert r.status_code == 404
