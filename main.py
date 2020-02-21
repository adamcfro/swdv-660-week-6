import logging
import logstash
import sys
import time

logger = logging.getLogger('python-logstash-logger')
logger.setLevel(logging.INFO)
logger.addHandler(logstash.LogstashHandler('3.133.157.171', 5959, version=1))


def factorial(n):
    """A simple program for calculating factorials."""
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


def main(num):
    if type(num) != int:
        logger.error('python-logstash - TypeError. Input must be integer.')
    elif num < 0:
        logger.warning(
            'python-logstash - ValueError: There are no factorials for negative numbers.')
    elif num == 0:
        return 1
    else:
        return factorial(num)


main(5)
main(0)
main(-2)
main("a")
