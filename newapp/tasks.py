from celery.utils.log import get_task_logger
from celery import shared_task

logger = get_task_logger(__name__)

@shared_task
def test_task():
    logger.info('Testing Celery with Test Function!')
    return 'Success'
