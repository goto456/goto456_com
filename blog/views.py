#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################################################
# File Name: views.py
# Author: Wang Biwen
# mail: wangbiwen88@126.com
# Created Time: 2016.01.09
#########################################################################

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import Http404
from models import Article

# Create your views here.
def home(request):
    post_list = Article.objects.all()
    return render_to_response('home.html', {'post_list': post_list})

def detail(request, id):
    try:
        post = Article.objects.get(id = int(id))
    except Article.DoesNotExit:
        raise Http404
    return render_to_response('post.html', {'post': post})

