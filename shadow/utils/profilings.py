# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
import datetime

from shadow.utils.loggers import info

def log_time(func):
  def wrapper(*args, **kwargs):
    begin = datetime.datetime.now()
    func(*args, **kwargs)
    end = datetime.datetime.now()

    timedelta = end - begin
    info("func %s processed in %f" %(func.__name__,
                  float(timedelta.total_seconds())))
    return func
  return wrapper

def log_n_time(n=100):
  def wrap(func):
    def wrapper(*args, **kwargs):
      begin = datetime.datetime.now()
      res = func(*args, **kwargs)
      for _ in range(n-1):
        res = func(*args, **kwargs)
      end = datetime.datetime.now()

      timedelta = end - begin
      info("func %s processed %d times in %.4f" %(func.__name__, n, float(timedelta.total_seconds())))
      info("func %s processed one time in %.4f" %(func.__name__, float(timedelta.total_seconds()/n)))
      return res

    return wrapper
  return wrap

def benchmark(func, n=100, *args, **kwargs):
  begin = datetime.datetime.now()
  for _ in range(n):
    func(args, kwargs)
  end = datetime.datetime.now()

  timedelta = end - begin
  info("func %s processed %d times in %.4f" %(func.__name__, n, float(timedelta.total_seconds())))
  info("func %s processed one time in %.4f" %(func.__name__, float(timedelta.total_seconds()/n)))