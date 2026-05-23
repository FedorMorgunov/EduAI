from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query

from app.models.quiz import Quiz, QuizCreate, QuizUpdate
from app.services import quiz_service

router = APIRouter()


@router.get("/", response_model=List[Quiz])
def list_quizzes(
    topic: Optional[str] = Query(None),
    difficulty: Optional[int] = Query(None, ge=1, le=5),
):
    return quiz_service.list_quizzes(topic=topic, difficulty=difficulty)


@router.post("/", response_model=Quiz, status_code=201)
def create_quiz(data: QuizCreate):
    return quiz_service.create_quiz(data)


@router.get("/{quiz_id}", response_model=Quiz)
def get_quiz(quiz_id: int):
    quiz = quiz_service.get_quiz(quiz_id)
    if quiz is None:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return quiz


@router.patch("/{quiz_id}", response_model=Quiz)
def update_quiz(quiz_id: int, data: QuizUpdate):
    quiz = quiz_service.update_quiz(quiz_id, data)
    if quiz is None:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return quiz


@router.delete("/{quiz_id}", status_code=204)
def delete_quiz(quiz_id: int):
    if not quiz_service.delete_quiz(quiz_id):
        raise HTTPException(status_code=404, detail="Quiz not found")
