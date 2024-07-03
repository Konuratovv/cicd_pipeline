#!/usr/bin/env bash

set -e

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver
