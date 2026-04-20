# Cookiecutter API Template

A professional FastAPI microservice template using Clean Architecture, uv for package management, and best practices for Python development.

## Features

- **Clean Architecture** - Domain, Application, Config, Ports and Adapters
- **FastAPI** - Modern, high-performance web framework
- **uv** - Fast Python package manager
- **Configuration** - Environment-based settings with pydantic-settings
- **Docker** - Multi-stage Dockerfile for production + docker-compose for local development
- **CI/CD** - GitHub Actions with ruff, mypy, pytest, and coverage
- **Testing** - pytest with httpx for async tests
- **Cruft** - Template versioning for easy updates

## Ventajas

- Arranque rápido de proyectos API
- Separación clara de responsabilidades
- Facilita pruebas y mantenimiento
- Compatible con despliegue en entornos modernos

## Requirements

- Python {{cookiecutter.python_version }}
- [uv](https://github.com/astral-sh/uv) - Install with: `curl -LsSf https://astral.sh/uv/install.sh | sh`

## Quick Start

```bash
# Install cruft
pip install cruft

# Create a new project from this template
cruft create https://github.com/JeanGC970520/microservice_template.git

# Or with GitHub CLI shorthand
cruft create gh:your-username/cookiecutter-microservice
```
