setup-virtualenv:
	python3 -m pip install virtualenv
	virtualenv venv
	. venv/bin/activate # BUG Not work

install-dev-deps: setup-virtualenv
	pip install --upgrade pip
	pip install -r requirements-dev.txt

install: setup-virtualenv
	pip install -r requirements.txt

prepare-dev-env: install-dev-deps install
	pre-commit install

lint:
	pylint gt_sat_api
	pylint tests

typehint:
	mypy gt_sat_api
	mypy tests

test:
	pytest --cov=gt_sat_api tests --junitxml=report.xml

coverage-html: test
	coverage html

lint-format:
	black -l 100 --check .

review: lint-format lint # TODO typehint test

format:
	isort .
	black -l 100 .

clean: check
	find src -type f -name "*.pyc" -delete
	find tests -type f -name "*.pyc" -delete
	find src -type d -name "__pycache__" -delete
	find tests -type d -name "__pycache__" -delete
	rm -rf .mypy_cache
	rm -rf .pytest_cache

check:
	@echo -n "Are you sure? [y/N] " && read ans && [ $${ans:-N} = y ]

create_wheel:
	python setup.py bdist_wheel

publish:
	twine upload dist/*
