install:
	pip3 install -r requirements.txt
	pip3 install -e .

install-dev:
	pip3 install -r requirements-dev.txt -r requirements-test.txt
	pre-commit install

install-test:
	pip3 install -r requirements-test.txt
	pip3 install -e .

run:
	python3 src/wurst_wuest

test:
	pytest

pre-commit:
	pre-commit run --all-files
