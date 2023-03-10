.PHONY: all
all: init run test build

.PHONY: init
init:
	@echo "๐ Start project dependencies"
	@python -m venv venv && source venv/bin/activate
	@pip install -r requirements.txt

.PHONY: run
run:
	@echo "๐ Running"
	@python main.py

.PHONY: test
test:
	@echo "๐งช Running tests"
	@python -m unittest discover -v

.PHONY: build
build:
	@echo "๐ Building"
	@pip freeze > requirements.txt