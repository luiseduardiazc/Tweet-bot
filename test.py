# for manage loop time
import time
from timeloop import Timeloop
from datetime import timedelta
import logging
import os

tl = Timeloop()
logger = logging.getLogger()

@tl.job(interval=timedelta(seconds=30))
def make_tweet():
    """ test """
    logger.info("run test")
    key = os.getenv("CONSUMER_KEY")
    print(key)


if __name__ == "__main__":
    tl.start(block=True)