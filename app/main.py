from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.routes import health, lessons, quizzes
from app.services import lesson_service, quiz_service
from app.models.lesson import LessonCreate
from app.models.quiz import QuizCreate, QuizQuestion, QuizOption

app = FastAPI(
    title="EduAI",
    description="AI-powered educational platform — quizzes and lessons API",
    version="0.1.0",
)


@app.on_event("startup")
def seed_demo_data():
    _seed_lessons()
    _seed_quizzes()


def _seed_lessons():
    demo_lessons = [
        LessonCreate(
            title="Introduction to Python",
            topic="Python",
            content=(
                "Python is a high-level, interpreted programming language known for its "
                "clear syntax and readability. It supports multiple programming paradigms "
                "including procedural, object-oriented, and functional programming. "
                "Python's extensive standard library and vibrant ecosystem make it ideal "
                "for web development, data science, automation, and AI."
            ),
            difficulty=1,
        ),
        LessonCreate(
            title="Object-Oriented Programming",
            topic="Python",
            content=(
                "Object-Oriented Programming (OOP) organises code into classes and objects. "
                "Key concepts: Encapsulation bundles data and methods together. "
                "Inheritance allows a class to reuse behaviour from a parent class. "
                "Polymorphism lets different classes respond to the same interface. "
                "Abstraction hides implementation details behind a clean API."
            ),
            difficulty=3,
        ),
        LessonCreate(
            title="Linear Algebra Basics",
            topic="Math",
            content=(
                "Linear algebra is the branch of mathematics concerning vectors, matrices, "
                "and linear transformations. Core topics include: vectors and vector spaces, "
                "matrix operations (addition, multiplication, transpose), determinants, "
                "eigenvalues and eigenvectors. Linear algebra underpins machine learning, "
                "computer graphics, and physics simulations."
            ),
            difficulty=2,
        ),
        LessonCreate(
            title="Neural Networks 101",
            topic="AI / ML",
            content=(
                "A neural network is a computational model inspired by the brain. "
                "It consists of layers of neurons: an input layer, one or more hidden layers, "
                "and an output layer. Each neuron applies a weighted sum followed by an "
                "activation function. Training adjusts weights via backpropagation and "
                "gradient descent to minimise a loss function."
            ),
            difficulty=4,
        ),
        LessonCreate(
            title="REST APIs with FastAPI",
            topic="Web Dev",
            content=(
                "FastAPI is a modern Python web framework for building REST APIs. "
                "It uses Python type hints to validate request/response data via Pydantic, "
                "and auto-generates interactive OpenAPI documentation. Key features: "
                "path and query parameters, request bodies, dependency injection, "
                "async support, and automatic data serialisation."
            ),
            difficulty=2,
        ),
    ]
    for data in demo_lessons:
        lesson_service.create_lesson(data)


def _seed_quizzes():
    def opt(*pairs):
        return [QuizOption(label=l, text=t) for l, t in pairs]

    demo_quizzes = [
        QuizCreate(
            title="Python Fundamentals",
            topic="Python",
            difficulty=1,
            questions=[
                QuizQuestion(
                    question="Which keyword is used to define a function in Python?",
                    options=opt(("A", "func"), ("B", "def"), ("C", "define"), ("D", "fn")),
                    correct_label="B",
                ),
                QuizQuestion(
                    question="What data type does type([]) return?",
                    options=opt(("A", "array"), ("B", "tuple"), ("C", "list"), ("D", "dict")),
                    correct_label="C",
                ),
                QuizQuestion(
                    question="Which operator is used for exponentiation in Python?",
                    options=opt(("A", "^"), ("B", "**"), ("C", "^^"), ("D", "exp")),
                    correct_label="B",
                ),
                QuizQuestion(
                    question="What does len('hello') return?",
                    options=opt(("A", "4"), ("B", "6"), ("C", "5"), ("D", "None")),
                    correct_label="C",
                ),
            ],
        ),
        QuizCreate(
            title="Math for ML",
            topic="Math",
            difficulty=3,
            questions=[
                QuizQuestion(
                    question="What is the dot product of vectors [1,0] and [0,1]?",
                    options=opt(("A", "1"), ("B", "0"), ("C", "-1"), ("D", "undefined")),
                    correct_label="B",
                ),
                QuizQuestion(
                    question="What does the determinant of an identity matrix equal?",
                    options=opt(("A", "0"), ("B", "-1"), ("C", "1"), ("D", "∞")),
                    correct_label="C",
                ),
                QuizQuestion(
                    question="Which activation function outputs values between 0 and 1?",
                    options=opt(("A", "ReLU"), ("B", "Tanh"), ("C", "Sigmoid"), ("D", "Softmax")),
                    correct_label="C",
                ),
            ],
        ),
        QuizCreate(
            title="Web Dev Basics",
            topic="Web Dev",
            difficulty=2,
            questions=[
                QuizQuestion(
                    question="Which HTTP method is used to create a resource?",
                    options=opt(("A", "GET"), ("B", "PUT"), ("C", "POST"), ("D", "DELETE")),
                    correct_label="C",
                ),
                QuizQuestion(
                    question="What HTTP status code means 'Not Found'?",
                    options=opt(("A", "200"), ("B", "301"), ("C", "500"), ("D", "404")),
                    correct_label="D",
                ),
                QuizQuestion(
                    question="What does REST stand for?",
                    options=opt(
                        ("A", "Remote Execution State Transfer"),
                        ("B", "Representational State Transfer"),
                        ("C", "Resource Endpoint Service Template"),
                        ("D", "Relational Entity Sync Transfer"),
                    ),
                    correct_label="B",
                ),
            ],
        ),
    ]
    for data in demo_quizzes:
        quiz_service.create_quiz(data)


app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(health.router, tags=["health"])
app.include_router(lessons.router, prefix="/lessons", tags=["lessons"])
app.include_router(quizzes.router, prefix="/quizzes", tags=["quizzes"])


@app.get("/", include_in_schema=False)
def root():
    return FileResponse("app/static/index.html")
