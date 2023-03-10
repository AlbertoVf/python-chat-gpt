.PHONY: all
all: init run test build

.PHONY: init
init:
	@echo "🏗 Start project dependencies"
	@python -m venv venv && source venv/bin/activate
	@pip install -r requirements.txt

.PHONY: run
run:
	@echo "🏗 Running"
	@python main.py

.PHONY: test
test:
	@echo "🧪 Running tests"
	@python -m unittest discover -v

.PHONY: build
build:
	@echo "🏗 Building"
	@pip freeze > requirements.txt