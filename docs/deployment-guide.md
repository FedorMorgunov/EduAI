# Deployment Guide — EduAI

## Option A — Docker (рекомендуется, 1 шаг)

**Требования:** Docker Desktop или Docker Engine + Docker Compose v2.

```bash
docker compose up --build
```

Приложение будет доступно на `http://localhost:8000`.  
Swagger UI (интерактивная документация): `http://localhost:8000/docs`.

Остановить:
```bash
docker compose down
```

---

## Option B — Python virtualenv (локальная разработка)

**Требования:** Python 3.11+.

```bash
# 1. Клонировать репозиторий
git clone https://github.com/FedorMorgunov/EduAI.git
cd EduAI

# 2. Создать виртуальное окружение и активировать
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# 3. Установить зависимости
pip install -r requirements.txt

# 4. Запустить сервер
uvicorn app.main:app --reload
```

Swagger UI: `http://localhost:8000/docs`

---

## Option C — Cloud (Render / Railway)

### Render

1. Зарегистрируйтесь на [render.com](https://render.com).
2. New → **Web Service** → подключите репозиторий `FedorMorgunov/EduAI`.
3. Настройки:
   | Поле | Значение |
   |------|----------|
   | Runtime | Python 3 |
   | Build Command | `pip install -r requirements.txt` |
   | Start Command | `uvicorn app.main:app --host 0.0.0.0 --port $PORT` |
4. Нажмите **Create Web Service** → получите публичный URL вида `https://eduai-xxxx.onrender.com`.

### Railway

1. Установите CLI: `npm i -g @railway/cli`
2. Войдите: `railway login`
3. Инициализируйте и разверните:
   ```bash
   railway init
   railway up
   ```
4. Откройте URL: `railway open`

Railway автоматически обнаружит `Dockerfile` и соберёт контейнер.

---

## Проверка работоспособности

После любого способа развёртывания выполните:

```bash
curl http://localhost:8000/health
# {"status":"ok","service":"EduAI","version":"0.1.0"}
```

Или откройте `http://localhost:8000/docs` в браузере и нажмите **Try it out** на любом эндпоинте.

---

## Переменные окружения

На текущем этапе (v0.1.0) внешних переменных окружения не требуется — приложение использует in-memory хранилище.  
Для production-деплоя с базой данных добавьте переменную `DATABASE_URL` и обновите сервисный слой.

---

## Структура образа

```
python:3.11-slim   ← базовый образ (~50 MB)
  └── /app
        ├── requirements.txt   ← зависимости (FastAPI, uvicorn, pydantic)
        └── app/               ← исходный код
```

Итоговый размер образа: ~120 MB.

---

## Запуск тестов в контейнере

```bash
docker build -t eduai .
docker run --rm eduai python -m pytest tests/ -v
```
