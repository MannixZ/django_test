#!/usr/bin/env python
# encoding: utf-8
'''
@author: Mannix
@file: view.py
@time: 2019/12/2 18:24
@desc:
'''

from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello world ! django ~~')

def hello(request):
    return HttpResponse('hello hello hello')