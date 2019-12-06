#!/usr/bin/env python
# encoding: utf-8

from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.

def index(request):
    return HttpResponse('Hello wordl! django ~~')

def demo(request):
    return render(request, 'demo.html')

def page(request, num):
    try:
        num = int(num)
        return render(request, 'demo.html')
    except:
        raise Http404

def home(request, year="2018", month="01"):
    return HttpResponse("获取当前页面home时间标签: %s年%s月" % (year, month))

def home1(request):
    return render(request, 'home.html')

def yoyo(request):
    context = {}
    body = {}
    context['name'] = '悠悠'
    context['sex'] = '男'
    body['mouth'] = '嘴'
    return render(request, 'yoyo.html', context)

def page1(request):
    context = {"name": "dawang", "sex": "男同学"}
    return render(request, 'page1.html', context)

def child(request):
    content = {'ads': ['1', '2', '3', 'abc', 'afs']}
    return render(request, 'child.html', content)