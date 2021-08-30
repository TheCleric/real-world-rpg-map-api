install:
	pip install -r requirements-dev.txt

run-local:
	uvicorn --port 5000 --host 127.0.0.1 api.main:app --reload
