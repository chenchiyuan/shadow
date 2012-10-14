# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from datetime import datetime

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