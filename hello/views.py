#!/usr/bin/env python
# encoding: utf-8

from django.shortcuts import render
from django.http import HttpResponse, Http404
from hello.models import User

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

# 测试qq号访问页面
def test_qq(request):
    '''请求页面'''
    return render(request, 'get_demo.html')

# 提交后返回页面
def result_qq(request):
    '''返回结果'''
    if request.method == "GET":
        # 获取提交的数据
        r = request.GET.get('q', None) # key就是前面输入框里的name属性对应值name="q"
        res = " "
        try:
            if int(r) % 2:
                res = "大吉大利!"
            else:
                res = "恭喜发财!"
        except:
            res = "请输入正确QQ号!"

        return HttpResponse("测试结果: %s" % res)
    else:
        render(request, 'get_demo.html')

def user(request):
    '''请求页面-返回结果'''
    res = ""
    if request.method == 'GET':
        # 获取提交的数据
        n = request.GET.get('name', None)
        res = User.objects.filter(user_name="%s" % n)
        try:
            res = res[0].mail
        except:
            res = "未查询到数据"
        return render(request, 'name.html', {'email': res})
    else:
        return render(request, 'name.html', {'email': res})