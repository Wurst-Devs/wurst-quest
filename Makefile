install:
	pip3 install -r requirements.txt
	pre-commit install

run:
	python3 src
