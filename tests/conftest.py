import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.services import lesson_service, quiz_service


@pytest.fixture(autouse=True)
def reset_stores():
    lesson_service.reset()
    quiz_service.reset()
    yield
    lesson_service.reset()
    quiz_service.reset()


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def SAMPLE_LESSON():
    return {
        "title": "Introduction to Python",
        "topic": "Python",
        "content": "Python is a high-level programming language.",
        "difficulty": 1,
    }


@pytest.fixture
def SAMPLE_QUIZ():
    return {
        "title": "Python Basics Quiz",
        "topic": "Python",
        "difficulty": 1,
        "questions": [
            {
                "question": "What keyword defines a function in Python?",
                "options": [
                    {"label": "A", "text": "func"},
                    {"label": "B", "text": "def"},
                    {"label": "C", "text": "define"},
                    {"label": "D", "text": "function"},
                ],
                "correct_label": "B",
            }
        ],
    }
