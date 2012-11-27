# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

def func_section(before_chain=[], after_chain=[]):
  def func_wrap(func):
    def wrap(*args, **kwargs):
      for before_func in before_chain:
        try:
          before_func(*args, **kwargs)
        except Exception:
          continue
      res = func(*args, **kwargs)

      for after_func in after_chain:
        try:
          after_func(*args, **kwargs)
        except Exception:
          continue
      return res
    return wrap
  return func_wrap

def example():
  def before_saying(self):
    print("I know your name %s" % self.name)

  def before_saving(self):
    print("I will notify your name %s" % self.name)

  def after_saving(self):
    print("After saving your name %s " % self.name)

  def done(self):
    print("Everything is ok %s " % self.name)

  class FuncTest():
    def __init__(self, name):
      self.name = name

    def __i_know_you(self):
      print("I know you guy %s " % self.name)

    @func_section(before_chain=[__i_know_you, before_saying, before_saving],
      after_chain=[after_saving, done])
    def save(self):
      print("Save name %s " % self.name)
      return self.name

  test = FuncTest(name=u'chenchiyuan')
  return test.save()