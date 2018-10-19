# Python Project Makefile

.PHONY: requirements.txt
.PHONY: help
.PHONY: test


help:
	@echo "Makefile rules:"
	@echo "   help    - This."
	@echo "   test    - Run unit-tests."

init:
	pip install -r requirements.txt

test:
	nosetests tests

requirements.txt:
	pip freeze > requirements.txt

clean:
	find . -name "__pycache__" -delete
	find . -name"*.py[oc]" -delete
