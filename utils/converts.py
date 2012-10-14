# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

def to_unicode(item):
  if not item:
    return u''

  if isinstance(item, str):
    return item.decode('utf-8')
  elif isinstance(item, unicode):
    return item
  else:
    return unicode(item, 'utf-8')

def to_str(item):
  if not item:
    return u''.encode('utf-8')

  if isinstance(item, unicode):
    return item.encode('utf-8')
  elif isinstance(item, str):
    return item
  else:
    return str(item)

