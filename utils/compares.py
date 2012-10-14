# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

def base_cmp(a, b):
  return -1 if a <= b else 1

def cmp_factory(func):
  """
  Get comparable item by func, and return cmp function
  """
  def real_cmp(a, b):
    return -1 if func(a) <= func(b) else 1

  return real_cmp
  