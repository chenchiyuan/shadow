# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

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
