#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################################################
# File Name: tt.py
# Author: Wang Biwen
# mail: wangbiwen88@126.com
# Created Time: 2016.01.09
#########################################################################

from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=100)
  category = models.CharField(max_length=50, blank=True)
  date_time = models.DateTimeField(auto_now_add=True)
  content = models.TextField(blank=True, null=True)

  def get_absolute_url(self):
      path = reverse('detail', kwargs={'id': self.id})
      return 'http://127.0.0.1:8000%s' % path

  def __unicode__(self):
    return self.title

  class Meta:
    ordering = ['-date_time']

