SHELL = /bin/bash

# Environment
venv:
	python3 -m venv fastapi-react_env
	source fastapi-react_env/bin/activate && \
	python3 -m pip install pip setuptools wheel && \
	python3 -m pip install --upgrade pip && \
	python3 -m pip install -e .[dev] && \
	pre-commit install && \
	pre-commit autoupdate


# Style
style:
	black .
	flake8 fastapi-react/
	python3 -m isort -rc fastapi-react/

# Test
test:
	python3 -m flake8 ./fastapi-react ./tests
	python3 -m mypy ./fastapi-react ./tests
	# https://stackoverflow.com/a/55095253
	python -m pytest -s --durations=0 --disable-warnings ./fastapi-react/ tests/
