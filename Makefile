TARGET := ci/

quick: install check_black check_mypy quick_test lint check_isort
all: quick test

install:
	poetry install

check_black:
	poetry run black --check $(TARGET)

check_mypy:
	poetry run mypy $(TARGET)

quick_test:
	poetry run pytest -m 'not external' -q --disable-warnings $(TARGET)

test:
	poetry run pytest -v $(TARGET)

lint:
	poetry run flake8 $(TARGET)

check_isort:
	# -rc -> recursive
	poetry run isort --check-only -rc $(TARGET)

# CI
# Note: CI caches the ~/.cache dir

ci_venv:
	python -m venv ~/.cache/virtualenv

ci_setup: ci_venv
	# ; \ -- run command in a single shell (so that it runs in virtualenv)
	. ~/.cache/virtualenv/bin/activate; \
	python -m pip install --upgrade pip poetry wheel; \
	poetry config cache-dir ~/.cache/poetry; \
	poetry config virtualenvs.create false; \
	poetry env use system; \
