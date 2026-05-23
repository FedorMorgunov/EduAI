from pydantic import BaseModel, Field
from typing import Optional


class LessonCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    topic: str = Field(..., min_length=1, max_length=100)
    content: str = Field(..., min_length=1)
    difficulty: int = Field(1, ge=1, le=5)


class Lesson(LessonCreate):
    id: int

    model_config = {"from_attributes": True}


class LessonUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    topic: Optional[str] = Field(None, min_length=1, max_length=100)
    content: Optional[str] = Field(None, min_length=1)
    difficulty: Optional[int] = Field(None, ge=1, le=5)
