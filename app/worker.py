import os
import sys
import logging
from celery import Celery
from celery.signals import after_setup_logger


app = Celery()
app.conf.update({
    'broker_url': os.environ['CELERY_BROKER_URL'],
    'imports': ('tasks', ),
    'task_serializer': 'json',
    'result_serializer': 'json',
    'accept_content': ['application/json'],
    'result_backend ': os.environ['CELERY_RESULT_BACKEND']
})


@after_setup_logger.connect
def setup_loggers(logger, *args, **kwargs):
    logger.info(f'Customize Celery logger, default handler: {logger.handlers[0]}')
    # uncomment the following line to make the banner appear in the docker logs
    # logger.addHandler(logging.StreamHandler(sys.stdout)) 
