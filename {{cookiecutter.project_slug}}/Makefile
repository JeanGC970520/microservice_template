.PHONY: help install test run up down logs lint format

help:
	@echo "Commands:"
	@echo "  make install   Install dependencies"
	@echo "  make test      Run tests"
	@echo "  make run       Run app locally"
	@echo "  make up        Start docker-compose"
	@echo "  make down      Stop docker-compose"
	@echo "  make logs      Tail docker-compose logs"
	@echo "  make lint      Run linter"
	@echo "  make format    Format code"

install:
	uv pip install -r pyproject.toml

test:
	uv run pytest

run:
	uv run uvicorn order_worker.main:app --reload

up:
	docker compose -f docker/docker-compose.yml up --build -d

down:
	docker compose -f docker/docker-compose.yml down

logs:
	docker compose -f docker/docker-compose.yml logs -f

lint:
	ruff check .

format:
	ruff format .