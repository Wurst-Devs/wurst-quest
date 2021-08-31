install:
	pip3 install -r requirements.txt
	pip3 install -e .

install-dev:
	pip3 install -r requirements.txt -r requirements-dev.txt -r requirements-test.txt
	pre-commit install

install-test:
	pip3 install -r requirements.txt -r requirements-test.txt
	pip3 install -e .

run:
	wurst-quest

test:
	pytest

pre-commit:
	pre-commit run --all-files
