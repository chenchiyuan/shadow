# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

def smart_print(items, title='', format_item_func=None):
  if title:
    print("########## %s ##########" % title)

  if isinstance(items, (list, tuple)):
    for item in items:
      smart_print(item)
  elif isinstance(items, dict):
    for item in items.items():
      smart_print(item)
  elif isinstance(items, (int, long, float, bool, basestring)):
    print(items)
  else:
    printable_items = items if not format_item_func else format_item_func(items)
    print(printable_items)
