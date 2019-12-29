import xadmin
# from django.contrib import admin
from hello import models
from hello.models import User, Person

class ControUser(object):
    '''自定义列表中栏目 添加list_display 属性'''
    list_display = ('user_name', 'psw', 'mail')
    # 搜索条件user_name
    search_fields = ('user_name', )

class ControlArticle(object):
    # 显示的字段
    list_display = ('title', 'body', 'auth', 'create_time', 'update_time')
    # 搜索条件
    search_fields = ('title', )
    # 按字段排序 -表示降序
    ordering = ('create_time', )

    # 每页显示10条
    list_per_page = 10

    # 可编辑字段
    list_editable = ('auth', )

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('title', 'body')

    # 过滤器
    list_filter = ('auth', 'title')

    # 时间分层
    date_hierarchy = 'create_time'

class ControBank(object):
    # 显示的字段
    list_display = ['bank_name', 'city', 'point']

class ControCardInfo(object):
    # 显示的字段
    list_display = ['card_id', 'card_name', 'info']

class ControAuther(object):
    list_display = ['name', 'city', 'mail']

class ControBook(object):
    list_display = ['book_name', '作者']

    def 作者(self, obj):
        return [a.name for a in obj.auth.all()]

class MoreInfo(object):
    model = models.CardDetail

class ControCard(object):
    list_display = ['card_id', 'card_user', 'add_time', "电话", "城市"]

    # 在Card页面显示更多信息CardDetail
    inlines = [MoreInfo]

    # 查询关联表的tel字段
    def 电话(self, obj):
        return obj.carddetail.tel

    def 城市(self, obj):
        return obj.carddetail.city

class ControTeacher(object):
    list_display = ['teacher_name', 'tel', 'mail']

class ControStudent(object):
    list_display = ['student_id', 'name', 'age', '老师']

    def 老师(self, obj):
        return [x.teacher_name for x in obj.teacher.all()]


# 注册Article表
xadmin.site.register(models.Article, ControlArticle)

# Register your models here.
xadmin.site.register(models.User, ControUser)
xadmin.site.register(models.Person)
xadmin.site.register(models.Bank, ControBank)
xadmin.site.register(models.CardInfo, ControCardInfo)
xadmin.site.register(models.Auther, ControAuther)
xadmin.site.register(models.Book, ControBook)
xadmin.site.register(models.Card, ControCard)
xadmin.site.register(models.Teacher, ControTeacher)
xadmin.site.register(models.Student, ControStudent)

xadmin.site.site_header = 'xx 项目管理系统'
xadmin.site.site_title = '登录系统后台'
xadmin.site.index_title = '后台管理'
