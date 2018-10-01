import os
import logging
import traceback
import time
from worker import app


logger = logging.getLogger(__name__)


@app.task(bind=True)
def task(self):
    logger.info('Run task')
    time.sleep(0.2)
    return 1