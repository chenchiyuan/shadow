# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from shadow.utils.encodes import md5_all, md5_encode
from shadow.utils.outputs import smart_print

import json
import os

class FunctionCache(object):
  def __init__(self, filename):
    self.caches = {}
    self.filename = filename or 'tmp/function.json'

  def _do_hash(self, func_name, unique_id='', *args, **kwargs):
    if unique_id:
      return unique_id
    else:
      fun_md5 = md5_all(func_name)
      args_md5 = md5_all(args)
      kwargs_md5 = md5_all(kwargs)


    hash_seq = [fun_md5, args_md5, kwargs_md5]
    return md5_encode(';'.join(hash_seq))

  def record(self, func_name, unique_id='', *args, **kwargs):
    key = self._do_hash(func_name, unique_id, *args, **kwargs)
    self.caches.update({key: True})

  def performed(self, func_name, unique_id='', *args, **kwargs):
    key = self._do_hash(func_name, unique_id, *args, **kwargs)
    return self.caches.has_key(key)

  def to_file(self):
    file = open(self.filename, 'w')
    for key in self.caches.keys():
      line = '%s\n' % key
      file.write(line.encode('utf-8'))
    file.close()

  @classmethod
  def read_file(cls, filename):
    if not os.path.exists(filename):
      return cls(filename)

    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    instance = cls(filename)

    for line in lines:
      hash_key = line[:-1]
      instance.caches.update({hash_key: True})
    return instance

def func_cache(instance, show=True, unique_id=''):
  def wrap(func):
    def wrapper(*args, **kwargs):
      if instance.performed(func.__name__, unique_id, *args, **kwargs):
        return

      try:
        res = func(*args, **kwargs)
      except Exception, err:
        if show:
          smart_print(args)
          smart_print(kwargs)
        raise err
      instance.record(func.__name__, unique_id, *args, **kwargs)
      return res

    return wrapper
  return wrap

cache = FunctionCache('/tmp/cache.info')

@func_cache(instance=cache)
def hello():
  print("Hello World")

class Test(object):
  @func_cache(instance=cache)
  def hello_tiantian(self):
    print("Hello Tian")

def example():
  t = Test()
  for _ in xrange(100):
    hello()
    t.hello_tiantian()
  cache.to_file()

if __name__ == '__main__':
  example()