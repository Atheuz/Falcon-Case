#!/bin/bash
celery -E -A main.celery worker --loglevel=info
python manage.py runserver 0.0.0.0:8000