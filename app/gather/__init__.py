from __future__ import absolute_import

from celery import Celery

celery = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0', include=['gather.tasks'])