"""Unit tests for the health-check endpoint."""


def test_health_returns_200(client):
    response = client.get("/health")
    assert response.status_code == 200


def test_health_response_shape(client):
    data = client.get("/health").json()
    assert data["status"] == "ok"
    assert data["service"] == "EduAI"
    assert "version" in data
