VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

# Basic Makefile for Python projects

install:
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) src/main.py

freeze:
	$(PIP) freeze > requirements.txt