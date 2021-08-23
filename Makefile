install:
	pip3 install -r requirements.txt -r requirements-dev.txt -r requirements-test.txt
	pre-commit install

run:
	python3 src

test:
	pytest

pre-commit:
	pre-commit run --all-files
