# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
import os
from urllibs.grab import grab
from utils.encodes import md5_encode

class LocalImageCache(object):
  def __init__(self, url, check=False, validate_size=0, cache_dir='/tmp/'):
    self.url = url
    self.md5_info = md5_encode(self.url)
    self.check = check
    self.validate_size = validate_size
    self.cache_dir = cache_dir

  def save(self, content=None):
    if not content:
      content = self.grab()

    if not content:
      return

    if self.check:
      validate = self.validate(content)
    else:
      validate = True

    if not validate:
      return

    file = open(self.get_filename(), 'w')
    file.write(content)
    file.close()

  def validate(self, content):
    if len(content) < self.validate_size and self.validate_size:
      return False
    return True

  def grab(self):
    try:
      data = grab(self.url)
    except Exception:
      return None
    else:
      return data

  def exists(self):
    filename = self.get_filename()
    return os.path.exists(filename), filename

  def get_path(self):
    path = os.path.join(self.cache_dir, self.md5_info[:5])
    return path

  def get_filename(self):
    path = self.get_path()
    if not os.path.exists(path):
      os.makedirs(path)

    file_path = os.path.join(path, '%s.jpg' % self.md5_info)
    return file_path