from celery.utils.log import get_task_logger
from celery import shared_task

logger = get_task_logger(__name__)

@shared_task
def task1():
    logger.info('Testing Task1')
    return 'Success'

@shared_task
def task2():
    logger.info('Testing Task2')
    return 'Success'