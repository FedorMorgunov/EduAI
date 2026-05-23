"""Unit tests for service-layer business logic."""
from app.models.lesson import LessonCreate, LessonUpdate
from app.models.quiz import QuizCreate, QuizOption, QuizQuestion, QuizUpdate
from app.services import lesson_service, quiz_service


# ── Lesson service ─────────────────────────────────────────────────────────────

def _make_lesson(**kwargs):
    defaults = {
        "title": "Test Lesson",
        "topic": "Testing",
        "content": "Some content",
        "difficulty": 2,
    }
    return LessonCreate(**{**defaults, **kwargs})


def test_create_and_retrieve_lesson():
    lesson = lesson_service.create_lesson(_make_lesson())
    assert lesson.id > 0
    retrieved = lesson_service.get_lesson(lesson.id)
    assert retrieved is not None
    assert retrieved.title == "Test Lesson"


def test_list_lessons_returns_all():
    lesson_service.create_lesson(_make_lesson(title="L1"))
    lesson_service.create_lesson(_make_lesson(title="L2"))
    assert len(lesson_service.list_lessons()) == 2


def test_list_lessons_topic_filter():
    lesson_service.create_lesson(_make_lesson(topic="Python"))
    lesson_service.create_lesson(_make_lesson(topic="Math"))
    results = lesson_service.list_lessons(topic="Python")
    assert len(results) == 1
    assert results[0].topic == "Python"


def test_update_lesson_fields():
    lesson = lesson_service.create_lesson(_make_lesson())
    updated = lesson_service.update_lesson(lesson.id, LessonUpdate(difficulty=5))
    assert updated is not None
    assert updated.difficulty == 5
    assert updated.title == lesson.title


def test_update_nonexistent_lesson_returns_none():
    result = lesson_service.update_lesson(9999, LessonUpdate(difficulty=3))
    assert result is None


def test_delete_lesson():
    lesson = lesson_service.create_lesson(_make_lesson())
    assert lesson_service.delete_lesson(lesson.id) is True
    assert lesson_service.get_lesson(lesson.id) is None


def test_delete_nonexistent_lesson_returns_false():
    assert lesson_service.delete_lesson(9999) is False


# ── Quiz service ───────────────────────────────────────────────────────────────

def _sample_question():
    return QuizQuestion(
        question="What is 2+2?",
        options=[
            QuizOption(label="A", text="3"),
            QuizOption(label="B", text="4"),
        ],
        correct_label="B",
    )


def _make_quiz(**kwargs):
    defaults = {
        "title": "Test Quiz",
        "topic": "Math",
        "difficulty": 1,
        "questions": [_sample_question()],
    }
    return QuizCreate(**{**defaults, **kwargs})


def test_create_and_retrieve_quiz():
    quiz = quiz_service.create_quiz(_make_quiz())
    assert quiz.id > 0
    retrieved = quiz_service.get_quiz(quiz.id)
    assert retrieved is not None
    assert retrieved.title == "Test Quiz"


def test_list_quizzes_difficulty_filter():
    quiz_service.create_quiz(_make_quiz(difficulty=1))
    quiz_service.create_quiz(_make_quiz(difficulty=3))
    results = quiz_service.list_quizzes(difficulty=3)
    assert len(results) == 1
    assert results[0].difficulty == 3


def test_update_quiz_title():
    quiz = quiz_service.create_quiz(_make_quiz())
    updated = quiz_service.update_quiz(quiz.id, QuizUpdate(title="New Title"))
    assert updated is not None
    assert updated.title == "New Title"


def test_delete_quiz_unit():
    quiz = quiz_service.create_quiz(_make_quiz())
    assert quiz_service.delete_quiz(quiz.id) is True
    assert quiz_service.get_quiz(quiz.id) is None
