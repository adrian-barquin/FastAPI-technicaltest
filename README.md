# FastAPI-technicaltest

# build imagen docker
docker compose up --build

# venv
uvicorn main:app --reload --app-dir app


# ACCESO

# Swagger
localhost:8000/docs

# API base
localhost:8000

# OpenAPI
localhost:8000/openapi.json