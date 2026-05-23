from fastapi import FastAPI

from app.routes import health, lessons, quizzes

app = FastAPI(
    title="EduAI",
    description="AI-powered educational platform — quizzes and lessons API",
    version="0.1.0",
)

app.include_router(health.router, tags=["health"])
app.include_router(lessons.router, prefix="/lessons", tags=["lessons"])
app.include_router(quizzes.router, prefix="/quizzes", tags=["quizzes"])
