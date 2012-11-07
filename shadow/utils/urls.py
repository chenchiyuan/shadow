# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from urlparse import urlparse

def get_url_domain(url):
  parse_result = urlparse(url)
  return '%s://%s/' % (parse_result.scheme, parse_result.netloc)