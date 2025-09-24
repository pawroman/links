default: check format test

check: check_ruff check_mypy

check_format:
    uv run ruff format --check .

check_ruff:
    uv run ruff check .

check_mypy:
    uv run mypy .

format:
    uv run ruff format .

format_isort:
    # isort formatting
    uv run ruff check --select I --fix .

test *ARGS:
    uv run pytest {{ARGS}}
