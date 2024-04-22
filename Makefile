PYTHON=python
FILENAME=code/web.py

run:
	export FLASK_DEBUG=True; export PORT=8080; ${PYTHON} ${FILENAME}

test:
	poetry run ${PYTHON} -m unittest discover code/src/ "test_*.py"

lint:
	poetry run flake8

isort:
	poetry run  isort . --check-only

isort-fix:
	poetry run  isort .

pre-commit:
	pre-commit run --all-files

freeze-dependencies:
	poetry export -f requirements.txt --output code/requirements.txt --without-hashes

coverage:
	poetry run coverage run -m  unittest discover code/ "test_*.py"
	poetry run coverage html --omit="*/__tests__/*,*/__init__*"
