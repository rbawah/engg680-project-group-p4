MAGENTA=`tput setaf 5`
RESET=`tput sgr0`

VENV_DIR := .venv
REQUIREMENTS := requirements.txt
PYTHON := python3

.DEFAULT_GOAL := help

help:
	@echo "Makefile for managing the Python environment and Docker setup"
	@echo "Usage:"
	@echo "  make venv            Create a Python virtual environment"
	@echo "  make install         Install Python requirements"
	@echo "  make clean           Remove the virtual environment and temporary files"

venv: $(VENV_DIR)
$(VENV_DIR):
	@echo "Creating Python virtual environment..."
	$(PYTHON) -m venv $(VENV_DIR)
	@echo "Virtual environment created in $(VENV_DIR)"

install: venv
	@echo "Activating virtual environment and installing requirements..."
	$(VENV_DIR)/bin/pip install --upgrade pip
	$(VENV_DIR)/bin/pip install -r $(REQUIREMENTS)
	@echo "Requirements installed successfully"
