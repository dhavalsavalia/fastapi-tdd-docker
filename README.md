# FastAPI TDD with Docker, Postgres, and Pytest

## Description
This is a simple project to demonstrate how to build a FastAPI application using Test Driven Development (TDD) as a development process. The project uses Docker and `docker compose` to containerize the application and Postgres database. Pytest is used as the testing framework.

## Project Structure
```bash
.
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── db.py
│   ├── models
│   │   ├── __init__.py
│   │   └── tortoise.py
├── db
│   ├── Dockerfile
│   └── create.sql
├── migrations
│   ├── models
├── .dockerignore
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── entrypoint.sh
├── Pipfile
├── Pipfile.lock
├── README.md
└── pyproject.toml
```

## Tech Stack
- FastAPI
- Docker
- Postgres
- Pytest
- Tortoise ORM
- Aerich

## Running the Project

1. Clone the repository
```bash
git clone https://github.com/dhavalsavalia/fastapi-tdd-docker.git
```
2. Change directory to the project directory
```bash
cd fastapi-tdd-docker
```
3. Build the Docker images
```bash
docker compose build --no-cache
```

4. Run the Docker containers
```bash
docker compose up -d --build
```

## Running Tests
To run the tests, execute the following command:
```bash
docker-compose exec web python -m pytest
```

## Running Migrations
To run migrations, execute the following command:
```bash
docker-compose exec web aerich upgrade
```