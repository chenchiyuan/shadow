# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
import urllib2

def grab(url):
  return urllib2.urlopen(url).read()