# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
import hashlib

def md5_encode(info):
  m = hashlib.md5()
  m.update(info)
  return m.hexdigest()