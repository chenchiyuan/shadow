# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
import hashlib
from shadow.utils.uniques import unicode_all

def md5_encode(info):
  m = hashlib.md5()
  m.update(info)
  return m.hexdigest()

def md5_all(item):
  info = unicode_all(item)
  return md5_encode(info)