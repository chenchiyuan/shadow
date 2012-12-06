# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.db import models

def find_all_models():
  all_models = models.get_models()
  for model in all_models:
    print(model._meta.verbose_name_plural)