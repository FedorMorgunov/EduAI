from typing import Dict, List, Optional

from app.models.quiz import Quiz, QuizCreate, QuizUpdate

_db: Dict[int, Quiz] = {}
_counter = 0


def _next_id() -> int:
    global _counter
    _counter += 1
    return _counter


def create_quiz(data: QuizCreate) -> Quiz:
    quiz = Quiz(id=_next_id(), **data.model_dump())
    _db[quiz.id] = quiz
    return quiz


def list_quizzes(topic: Optional[str] = None, difficulty: Optional[int] = None) -> List[Quiz]:
    quizzes = list(_db.values())
    if topic:
        quizzes = [q for q in quizzes if q.topic.lower() == topic.lower()]
    if difficulty is not None:
        quizzes = [q for q in quizzes if q.difficulty == difficulty]
    return quizzes


def get_quiz(quiz_id: int) -> Optional[Quiz]:
    return _db.get(quiz_id)


def update_quiz(quiz_id: int, data: QuizUpdate) -> Optional[Quiz]:
    quiz = _db.get(quiz_id)
    if quiz is None:
        return None
    updated = quiz.model_dump()
    for field, value in data.model_dump(exclude_none=True).items():
        updated[field] = value
    _db[quiz_id] = Quiz(**updated)
    return _db[quiz_id]


def delete_quiz(quiz_id: int) -> bool:
    if quiz_id not in _db:
        return False
    del _db[quiz_id]
    return True


def reset() -> None:
    """Reset in-memory store (test helper)."""
    global _counter
    _db.clear()
    _counter = 0
