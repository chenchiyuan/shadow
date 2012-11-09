# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from shadow.datetimes.formats import datetime_to_str
from shadow.utils.converts import to_unicode
from unidecode import unidecode

import re
import uuid
import unicodedata
from datetime import datetime

def unique_name():
  return to_unicode(uuid.uuid4()).replace('-', '')

def slugify(value):
  value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
  value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
  return re.sub('[-\s]+', '-', value)

def get_unique_slug(name, parent_slug='', prefix_loop=0):
  slug_list = []
  for _ in range(prefix_loop):
    slug_list.append('_')

  slug_list.append(unidecode(name))
  if parent_slug:
    slug_list.append(unidecode(parent_slug))
  return slugify('-'.join(slug_list))

def unicode_all(item):
  if not item:
    return ''

  if isinstance(item, (int, long, float)):
    return unicode(item)
  elif isinstance(item, basestring):
    return to_unicode(item)
  elif isinstance(item, (list, set, tuple)):
    result = []
    for aim in item:
      result.append(unicode_all(aim))
    return ''.join(result)
  elif isinstance(item, dict):
    result = []
    for key, value in item.items():
      result.append(unicode_all(key))
      result.append(unicode_all(value))
    return ''.join(result)
  elif isinstance(item, datetime):
    return datetime_to_str(item)

  items = item.__dict__
  return unicode_all(items)
