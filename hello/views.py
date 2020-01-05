#!/usr/bin/env python
# encoding: utf-8

from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from hello.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail, send_mass_mail, EmailMessage, EmailMultiAlternatives
import os
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

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

def register(request):
    '''注册页面'''
    res = ""
    if request.method == "POST":
        username = request.POST.get('username')
        psw = request.POST.get('password')
        mail = request.POST.get('mail')

        # 先查询数据库是否有此用户名
        user_lst = User.objects.filter(user_name=username)
        if user_lst:
            # 如果已经注册过，就给个提示
            res = "%s用户已被注册" % username
            return render(request, 'register.html', {'name': res})
        else:
            # 如果没被注册, 插入数据库

            # 第一种写法 -- 推荐
            user = User()
            user.user_name = username
            user.psw = make_password(psw)
            user.mail = mail
            user.save()

            # 第二种写法
            # user = User(user_name=username,
            #             psw=psw,
            #             mail=mail,
            #             )
            # user.save()
            return render(request, 'login.html', {'rename': res})
    return render(request, 'register.html')

def login(request):
    '''登录页面'''
    if request.method == "GET":
        return render(request, 'login.html')
    if request.method == "POST":
        # 先查询数据库是否有此用户名
        username = request.POST.get('username')
        psw = request.POST.get('password')
        # 查询用户名和密码
        user_obj = User.objects.filter(user_name=username).first()
        # 检验密码
        is_psw_true = check_password(psw, user_obj.psw)
        if user_obj:
            return HttpResponse('登录成功')
        else:
            return HttpResponse('用户名或密码错误')

def reset_psw(request):
    '''修改密码'''
    res = ""
    if request.method == "GET" :
        return render(request, 'reset_psw.html', {'msg': res})
    if request.method == "POST":
        username = request.POST.get('username')
        psw = request.POST.get('password')
        new_psw = request.POST.get('new')

        if psw == new_psw:
            res = '新密码和旧密码不能重复'
            return render(request, 'reset_psw.html', {'msg': res})
        else:
            # 先查询数据库是否有此用户名
            user_lst = User.objects.filter(user_name=username)
            if not user_lst:
                # 如果没这个用户
                res = "用户未注册: %s" % username
                return render(request, 'reset_psw.html', {'msg': res})

            else:
                # 如果注册过,判断密码对不对
                ret = User.objects.filter(user_name=username).first()
                # 校验密码
                is_psw_true = check_password(psw, ret.psw)
                if is_psw_true:
                    user = User()
                    user.psw = make_password(new_psw)
                    user.save()
                    res = "密码修改成功!"
                else:
                    res = "密码错误!"
                return render(request, 'reset_psw.html', {'msg': res})

def mail(request):
    send_mail('Subject here',
              'Here is the message',
              '317588213@qq.com',
              ['zmjbobo5@163.com'])
    return HttpResponse('邮件发送成功,收不到就去垃圾箱找吧')

def mail_html(request):
    '''发送html格式邮件'''
    h = '''
    <!DOCTYPE HTML>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>带图片的邮件</title>
    </head>
    <body>
    <a href="https://yuedu.baidu.com/ebook/902224ab27fff705cc1755270722192e4536582b" target="_blank">
        <p>pytest教程,点图片进入：<br>
        <img src="https://img2018.cnblogs.com/blog/1070438/201902/1070438-20190228112918941-704279799.png" height="160" width="270" />
        </p></a>
    <p>
    其它图片：<br>
    <img src="http://www.w3school.com.cn/i/eg_chinarose.jpg" height=150 width=300/></p>
    <p>请注意，插入动画图像的语法与插入普通图像的语法没有区别。</p>
    </body>
    </html>
    '''
    send_mail('Subject here',
              'hell',
              '317588213@qq.com',
              ['zmjbobo5@163.com'],
              fail_silently=False,
              html_message=h)
    return HttpResponse('邮件发送成功,收不到就去垃圾箱找找吧!')

def file_mail(request):
    '''发送附件'''
    email = EmailMessage(
        'Hello',
        'Body goes here',
        '317588213@qq.com',
        ['zmjbobo5@163.com', 'zmjbobo6@163.com'],
        ['zmjbobo7@163.com'],
        reply_to=['another@example.com'],
        headers={'Message-Id': 'foo'}
    )
    cur = os.path.dirname(os.path.realpath(__file__))
    # templates目录下有个a.png图片
    filepath = os.path.join(cur, "templates", "a.png")

    email.attach_file(filepath, mimetype=None)
    email.send()
    return HttpResponse('邮件发送成功,收不到就去垃圾箱找找吧')

def file_html_mail(request):
    '''发送附件 + html'''
    email = EmailMultiAlternatives(
        'Hello',
        'Body goes here',
        '317588213@qq.com',
        ['zmjbobo5@163.com', 'zmjbobo6@163.com'],
        ['zmjbobo7@163.com'],
        reply_to=['another@example.com'],
        headers={'Message-Id': 'foo'}
    )
    cur = os.path.dirname(os.path.realpath(__file__))
    # templates目录下有个a.png图片
    filepath = os.path.join(cur, "templates", "a.png")

    email.attach_file(filepath, mimetype=None)

    #添加正文 html
    h = '''
        <!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>带图片的邮件</title>
        </head>
        <body>
        <a href="https://yuedu.baidu.com/ebook/902224ab27fff705cc1755270722192e4536582b" target="_blank">
            <p>pytest教程,点图片进入：<br>
            <img src="https://img2018.cnblogs.com/blog/1070438/201902/1070438-20190228112918941-704279799.png" height="160" width="270" />
            </p></a>
        <p>
        其它图片：<br>
        <img src="http://www.w3school.com.cn/i/eg_chinarose.jpg" height=150 width=300/></p>
        <p>请注意，插入动画图像的语法与插入普通图像的语法没有区别。</p>
        </body>
        </html>
        '''
    email.attach_alternative(content=h, mimetype='text/html')
    email.send()
    return HttpResponse('邮件发送成功,收不到就去垃圾箱找找吧')

def loginView(request):
    '''登录'''
    if request.method == "POST":
        username = request.POST.get('username', '')
        psw = request.POST.get('password', '')
        user = authenticate(username=username, password=psw)
        if user is not None:
            if user.is_active:
                login(request, user=user)
                request.session['user'] = username
                return HttpResponseRedirect('/success')
        else:
            return render(request, 'login2.html', {'msg': '账号或密码错误!'})
    else:
        return render(request, 'login2.html', {'msg': ''})

@login_required
def successView(request):
    '''登录成功页'''
    return render(request, 'success.html', {'msg': ''})

def logoutView(request):
    '''退出登录'''
    logout(request)
    return render(request, 'login2.html', {'msg': ''})


