# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
import hashlib
from IPython.utils.py3compat import unicode_to_str
from shadow.utils.uniques import unicode_all

def md5_encode(info):
  m = hashlib.md5()
  m.update(info)
  return m.hexdigest()

def md5_all(item):
  info = unicode_all(item)
  info_str = unicode_to_str(info)
  return md5_encode(info_str)