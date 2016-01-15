#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################################################
# File Name: custom_markdown.py
# Author: Wang Biwen
# mail: wangbiwen88@126.com
# Created Time: 2016.01.13
#########################################################################

import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

register = template.Library() #自定义filter时必须加上

@register.filter(is_safe=True) #注册templa filter
@stringfilter #希望字符串作为参数
def custom_markdown(value):
    return mark_safe(markdown.markdown(value, 
        extensions=['markdown.extensions.fenced_code', 'markdown.extensions.codehilite'],
        safe_mode=True,
        enable_attributions=False))
