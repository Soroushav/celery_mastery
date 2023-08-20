import os
from celery import Celery

app = Celery('celeryworker')
app.config_from_object('celeryconfig')

@app.task
def add_numbers():
    return 'Worked!'