# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from datetime import datetime
from shadow.datetimes.timezone import is_naive, get_default_timezone, make_aware
from datetime import datetime as py_time

def format_date_time(dt):
  if not dt:
    return ''
  if not isinstance(dt, datetime):
    raise ValueError(u'can not format a incorrect datetime')

  now = datetime.now()
  time_str = dt.strftime('%H:%M')
  diff = now - dt
  if diff.days == 0:
    if diff.seconds < 60:
      return u'%s秒前' % diff.seconds
    if diff.seconds < 3600:
      return u'%s分钟前' % (diff.seconds / 60)
    return u'%s个小时前' % (diff.seconds / 3600)
  else:
    diff = now.date() - dt.date()

  if diff.days == 1:
    return u'昨天 ' + time_str
  elif diff.days == 2:
    return u'前天' + time_str
  elif diff.days < 15:
    return u'%s天前' % diff.days
  else:
    return dt.strftime('%y-%m-%d %H:%M')

def datetime_to_str(datetime, format='%Y-%m-%d %H:%M:%S'):
  if is_naive(datetime): # datetime to utc time
    datetime = to_aware_datetime(datetime)

  return datetime.strftime(format)

def str_to_datetime(str, format='%Y-%m-%d %H:%M:%S'):
  return to_aware_datetime(py_time.strptime(str, format))

def to_aware_datetime(value):
  time_zone = get_default_timezone()
  return make_aware(value, time_zone)