#!/bin/bash

set -e

if [ "$1" = 'local' ]; then
    poetry run python manage.py migrate
    poetry run python manage.py collectstatic --noinput

    exec poetry run python manage.py runserver 0.0.0.0:8000

else
    poetry run python manage.py collectstatic --noinput

    exec poetry run gunicorn -b 0.0.0.0:8000 --reuse-port project.wsgi:application

fi
