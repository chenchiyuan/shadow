# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

class DotDict(dict):
  def __getattr__(self, attr):
    return self.get(attr, None)

  __setattr__ = dict.__setitem__
  __delattr__ = dict.__delitem__