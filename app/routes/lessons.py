from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query

from app.models.lesson import Lesson, LessonCreate, LessonUpdate
from app.services import lesson_service

router = APIRouter()


@router.get("/", response_model=List[Lesson])
def list_lessons(topic: Optional[str] = Query(None)):
    return lesson_service.list_lessons(topic=topic)


@router.post("/", response_model=Lesson, status_code=201)
def create_lesson(data: LessonCreate):
    return lesson_service.create_lesson(data)


@router.get("/{lesson_id}", response_model=Lesson)
def get_lesson(lesson_id: int):
    lesson = lesson_service.get_lesson(lesson_id)
    if lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return lesson


@router.patch("/{lesson_id}", response_model=Lesson)
def update_lesson(lesson_id: int, data: LessonUpdate):
    lesson = lesson_service.update_lesson(lesson_id, data)
    if lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return lesson


@router.delete("/{lesson_id}", status_code=204)
def delete_lesson(lesson_id: int):
    if not lesson_service.delete_lesson(lesson_id):
        raise HTTPException(status_code=404, detail="Lesson not found")
