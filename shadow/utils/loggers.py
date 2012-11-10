# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
import os

try:
  import logging
  logger = logging.getLogger(__name__)
except ImportError:
  logger = None

if not logger:
  info = error = print
else:
  info = logger.info
  error = logger.error

def get_filebased_logger(filepath, lever=logging.DEBUG):
  logger = logging.getLogger(__name__)
  logger.setLevel(lever)

  handler = logging.FileHandler(filepath)
  handler.setLevel(logging.DEBUG)

  formatter = logging.Formatter('%(asctime)s %(lineno)d %(funcName)s %(message)s')
  handler.setFormatter(formatter)
  logger.addHandler(handler)
  return logger
