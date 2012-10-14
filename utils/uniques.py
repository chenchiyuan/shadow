# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from utils.converts import to_unicode
from unidecode import unidecode

import re
import uuid
import unicodedata

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

