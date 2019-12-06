#!/usr/bin/env python
# encoding: utf-8
'''
@author: Mannix
@file: testdb.py
@time: 2019/12/4 20:27
@desc:
'''

from django.http import HttpResponse

from hello.models import Test
from hello.models import User

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