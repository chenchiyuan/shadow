# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from shadow.utils.encodes import md5_encode
from shadow.utils.outputs import smart_print

import json
import os

class FunctionCache(object):
  def __init__(self, filename):
    self.caches = {}
    self.filename = filename or 'tmp/function.json'

  def _do_hash(self, func_name, unique_id='', *args, **kwargs):
    def dumps_smart(item):
      if not item:
        return ''
      else:
        try:
          return json.dumps(item)
        except:
          return json.dumps(item.__class__.__name__) # TODO

    hash_seq = [func_name, dumps_smart(args), json.dumps(kwargs), unique_id]
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

def func_cache(instance, unique_id=''):
  def wrap(func):
    def wrapper(*args, **kwargs):
      if instance.performed(func.__name__, unique_id, *args, **kwargs):
        return

      try:
        res = func(*args, **kwargs)
      except Exception, err:
        smart_print(args, "Args")
        smart_print(kwargs, "Kwargs")
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