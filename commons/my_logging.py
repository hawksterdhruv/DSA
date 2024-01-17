""" 
my_logging.py
Author : Dhruv Shah
"""
import logging

FORMAT = "%(name)s:%(levelname)s :: %(message)s"

# logging.basicConfig(level=logging.DEBUG, format=FORMAT)

logger = logging.getLogger("algo_debug")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(fmt=FORMAT)

handler = logging.StreamHandler()

handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)

logger.addHandler(handler)
