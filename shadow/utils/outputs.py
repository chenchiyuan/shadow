# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from datetime import datetime
from shadow.const import DATETIME_FORMAT

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

def json_item(item):
  if not item:
    return None

  if isinstance(item, (basestring, int, float, bool, long)):
    return item
  elif isinstance(item, (list, tuple, set)):
    return [json_item(i) for i in item]
  elif isinstance(item, dict):
    d = {}
    for name, value in item.items():
      d[name] = json_item(value)
    return d
  elif isinstance(item, datetime):
    return item.strftime(DATETIME_FORMAT)
  else:
    return item