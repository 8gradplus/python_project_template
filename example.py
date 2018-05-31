import logging
import sys
from helpers.logging import on_enter, on_exit, on_exception


import logging
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@on_exception(logger)
@on_exit(logger)
@on_enter(logger)
def divide(n: int):
    """This is a really stupid example
    - type and value should be checked instead of logged."""
    return 1/n


if __name__ == "__main__":

    # Example for logging
    divide(n=10) # no exception
    divide(n=0) # exception




