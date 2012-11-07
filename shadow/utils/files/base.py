# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

class FileWriter(object):
  def __init__(self, filename, data_seq=[]):
    self.filename = filename
    self.data_seq = data_seq

  def write(self):
    file = open(self.filename, 'w')
    for data in iter(self.data_seq):
      line = '%s\n' % data
      file.write(line.encode('utf-8'))
    file.close()

class FileReader(object):
  def __init__(self, filename):
    self.filename = filename

  def readlines(self):
    file = open(self.filename, 'r')
    lines = file.readlines()
    file.close()
    for line in lines:
      if not line:
        continue
      elif line.endswith('\n'):
        yield line[:-1]
      else:
        yield line