# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
import json
from shadow.utils.outputs import json_item

class BaseOutput(object):
  def __init__(self, queryset, file_path='',
               exclude=[], format='json', select_related={}):
    self.format = format
    self.exclude = exclude
    self.queryset = queryset
    self.file_path = file_path
    self.select_related = select_related

  def output(self, func=None):
    if not func:
      func = lambda s: s.__dict__

    def format_item(item):
      validate = {}
      item_info = func(item)
      for field, value in item_info.items():
        if field in self.exclude: continue
        elif field in self.select_related:
          validate.update({
            field: format_item(self.select_related[field].objects.get(value))
          })
        else:
          validate.update({field: value})
      return validate

    file = open(self.file_path, 'w')
    for item in self.queryset:
      info = json_item(format_item(item))
      info_str = json.dumps(info).encode('utf-8')
      file.write('%s\n' % info_str)
    file.close()

class BaseInput(object):
  def __init__(self, file_path=''):
    self.file_path = file_path

  def _do_read(self):
    file = open(self.file_path, 'r')
    lines = file.readlines()
    file.close()

    for line in lines:
      info = json.loads(line.decode('utf-8')[:-1])
      yield info

  def input(self, callback):
    json_info = self._do_read()
    for info in json_info:
      callback(info)
