import sys
from loguru import logger

logger.remove()
logger.add(sys.stderr, format="", colorize=False, backtrace=True)


@logger.catch
def decorated(x, y, z):
    raise NotImplementedError


def not_decorated(x, y, z):
    raise NotImplementedError


decorated(1)

with logger.catch():
    not_decorated(2)

try:
    not_decorated(3)
except TypeError:
    logger.exception("")
