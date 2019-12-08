#!/usr/bin/env python
# encoding: utf-8
'''
@author: Mannix
@file: testdb.py
@time: 2019/12/4 20:27
@desc:
'''

from django.http import HttpResponse, JsonResponse

from hello.models import Test
from hello.models import User
from django.core import serializers
import json
from django.forms.models import model_to_dict

# 数据库操作
def testdb(request):
    test1 = Test(name='haha')
    test1.save()
    return HttpResponse('hello_test添加name成功! 去看看吧')

# 新增数据
def add_user(request):
    test1 = User(user_name='haha',
                 psw='555',
                 mail='999@yy.com')
    test1.save()
    return HttpResponse('haha用户创建成功! 去看看吧')

# 更新数据
def update_psw(request):
    # 修改其中一个user_name='haha'的字段, 再save, 相当于SQL的UPDATE
    test2= User.objects.get(user_name='haha')
    test2.psw = '999'
    test2.save()

    # 另一种方式
    # Test.objects.filter(id=1).update(name='Google')

    # 修改所有列
    # Test.objects.all().update(name='Google')
    return HttpResponse('<p>密码修改成功</p>')

# 删除数据
def delete_user(request):
    # 删除user_name=haha的数据
    test3 = User.objects.get(user_name='haha')
    test3.delete()

    # 另一种方式
    # Test.objects.filter(id=1).delete()

    # 删除所有数据
    # Test.objects.all().delete()
    return HttpResponse('<p>删除成功</p>')

# 查询数据
def select_mail(request):

    # 方法1 可以查询单个结果直接换区mail值
    m = User.objects.get(user_name='haha').mail

    # 方法2 filter相当于SQL中的WHERE,可设置条件过滤结果
    # test4 = User.objects.filter(user_name='haha')

    # 查询结果是list,取下标后,获取mail字段的值
    # m = test4[0].mail

    return HttpResponse('<p>查询结果: %s</p>' % m)

# 查找User表数据
def slec_all(request):
    '''取出user表里面user_name、psw、mail全部数据'''
    users = ''
    psws = ''
    mails = ''
    ret = User.objects.all()

    # 返回queryset对象, 可迭代
    for i in ret:
        users += " " + i.user_name
        psws += " " + i.psw
        mails += " " + i.mail

    return HttpResponse('''<p>查询user结果：%s</p>
                            <p>查询psw结果：%s</p>
                            <p>查询psw结果：%s</p>''' % (users, psws, mails))

def sele_filter(request):
    '''获取user_name="haha" and psw="123456"对应的mail值
    查找为空时，返回null'''
    r = " "
    ret = User.objects.filter(user_name='haha',
                              psw='123456')
    try:
        r = ret[0].mail
    except:
        r = 'null'
    return HttpResponse('<p>查询结果: %s</p>' % (r))

def sele_values(request):
    '''可迭代的字典序列'''
    r = " "
    ret = User.objects.all().values("user_name", "mail")
    for i in ret:
        r += str(i)
    return HttpResponse('<p>查询结果: %s</p>' % r)

def sele_get(request):
    '''get返回唯一的查询结果'''
    r = " "
    ret = User.objects.get(user_name='haha')
    r = ret.user_name + ret.mail
    return HttpResponse('<p>查询结果: %s</p>' % r)

def sele_first_last(request):
    '''查询第一个和最后一个记录'''
    fir = User.objects.all().order_by('mail').first()
    f = fir.mail

    las = User.objects.all().order_by('mail').last()
    l = las.mail
    return HttpResponse('<p>查询第一个结果：%s</p> <p>查询最后结果：%s</p>' % (f, l))

def get_json(request):
    '''返回json数据'''
    data = {}
    a = User.objects.all()
    data['result'] = json.loads(serializers.serialize('json', a))
    return JsonResponse(data)

def to_dict(request):
    '''把返回的结果转成dict序列'''
    ret = User.objects.all()
    json_list = []
    for i in ret:
        json_dict = model_to_dict(i)
        json_list.append(json_dict)
    return JsonResponse(json_list, safe=False)

def json_data(request):
    '''values()获取的可迭代dict对象转List'''
    data = {}
    ret = User.objects.all().values()
    data['data'] = list(ret)
    return JsonResponse(data,
                        safe=False,
                        json_dumps_params={'ensure_ascii':False})