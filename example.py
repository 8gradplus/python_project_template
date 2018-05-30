import logging
import sys
from helpers.logging import on_enter, on_exit, on_exception
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


@on_exception(logger)
@on_exit(logger)
@on_enter(logger)
def divide(n: int):
    return 1/n


if __name__ == "__main__":

    divide(n=0)
