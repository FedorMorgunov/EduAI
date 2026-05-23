from typing import Dict, List, Optional

from app.models.lesson import Lesson, LessonCreate, LessonUpdate

_db: Dict[int, Lesson] = {}
_counter = 0


def _next_id() -> int:
    global _counter
    _counter += 1
    return _counter


def create_lesson(data: LessonCreate) -> Lesson:
    lesson = Lesson(id=_next_id(), **data.model_dump())
    _db[lesson.id] = lesson
    return lesson


def list_lessons(topic: Optional[str] = None) -> List[Lesson]:
    lessons = list(_db.values())
    if topic:
        lessons = [ls for ls in lessons if ls.topic.lower() == topic.lower()]
    return lessons


def get_lesson(lesson_id: int) -> Optional[Lesson]:
    return _db.get(lesson_id)


def update_lesson(lesson_id: int, data: LessonUpdate) -> Optional[Lesson]:
    lesson = _db.get(lesson_id)
    if lesson is None:
        return None
    updated = lesson.model_dump()
    for field, value in data.model_dump(exclude_none=True).items():
        updated[field] = value
    _db[lesson_id] = Lesson(**updated)
    return _db[lesson_id]


def delete_lesson(lesson_id: int) -> bool:
    if lesson_id not in _db:
        return False
    del _db[lesson_id]
    return True


def reset() -> None:
    """Reset in-memory store (test helper)."""
    global _counter
    _db.clear()
    _counter = 0
