# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

def distinct_list(seq, idfun=None):
  # order preserving
  if idfun is None:
    def idfun(x): return x
  seen = {}
  result = []
  for item in seq:
    marker = idfun(item)
    # in old Python versions:
    # if seen.has_key(marker)
    # but in new ones:
    if marker in seen: continue
    seen[marker] = 1
    result.append(item)
  return result