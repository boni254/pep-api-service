SHELL = /bin/bash -l

.PHONY: install/python install/pre-commit install test lint run copy/local/envs migrations deploy/local

install/python:
	poetry install --sync --with dev --no-root

install/pre-commit:
	poetry run pre-commit install

install: install/python install/pre-commit

test:
	DJANGO_ENVIRONMENT=test poetry run pytest -x --cov --failed-first tests

lint: install/pre-commit
	poetry run pre-commit run -a -v

copy/local/envs:
	cp .env-example .env

migrations: copy/local/envs
	poetry run python manage.py makemigrations --no-header -n ${name}

deploy/local:	copy/local/envs
	docker compose up -d --build

run:
	docker compose up rabbitmq -d
	/bin/bash -l config/docker/entrypoint.sh
