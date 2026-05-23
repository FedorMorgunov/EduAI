from pydantic import BaseModel, Field
from typing import List, Optional


class QuizOption(BaseModel):
    label: str
    text: str


class QuizQuestion(BaseModel):
    question: str
    options: List[QuizOption]
    correct_label: str


class QuizCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    topic: str = Field(..., min_length=1, max_length=100)
    difficulty: int = Field(1, ge=1, le=5)
    questions: List[QuizQuestion] = Field(..., min_length=1)


class Quiz(QuizCreate):
    id: int

    model_config = {"from_attributes": True}


class QuizUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    topic: Optional[str] = Field(None, min_length=1, max_length=100)
    difficulty: Optional[int] = Field(None, ge=1, le=5)
    questions: Optional[List[QuizQuestion]] = None
