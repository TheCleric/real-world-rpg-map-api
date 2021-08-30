autopep8: isort
	autopep8 -i --recursive api tests

ci: pytest mypy pylint

install:
	pip install -r requirements-dev.txt

isort:
	isort api tests

mypy:
	mypy api tests

pre-commit: autopep8 ci

pylint:
	pylint api tests

pytest:
	pytest tests --cov=api --cov-report=term-missing

run-local:
	uvicorn --port 5000 --host 127.0.0.1 api.main:app --reload
