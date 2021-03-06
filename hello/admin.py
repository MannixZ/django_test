from django.contrib import admin
from hello import models
from hello.models import User, Person

@admin.register(User)
class ControUser(admin.ModelAdmin):
    '''自定义列表中栏目 添加list_display 属性'''
    list_display = ('user_name', 'psw', 'mail')
    # 搜索条件user_name
    search_fields = ('user_name', )

class ControlArticle(admin.ModelAdmin):
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

class ControBank(admin.ModelAdmin):
    # 显示的字段
    list_display = ['bank_name', 'city', 'point']

class ControCardInfo(admin.ModelAdmin):
    # 显示的字段
    list_display = ['card_id', 'card_name', 'info']

class ControAuther(admin.ModelAdmin):
    list_display = ['name', 'city', 'mail']

class ControBook(admin.ModelAdmin):
    list_display = ['book_name', '作者']

    def 作者(self, obj):
        return [a.name for a in obj.auth.all()]

class MoreInfo(admin.StackedInline):
    model = models.CardDetail

@admin.register(models.Card)
class ControCard(admin.ModelAdmin):
    list_display = ['card_id', 'card_user', 'add_time']

    # 在Card页面显示更多信息CardDetail
    inlines = [MoreInfo]

# 注册Article表
admin.site.register(models.Article, ControlArticle)

# Register your models here.
# admin.site.register(models.User, ControUser)
admin.site.register(models.Person)
admin.site.register(models.Bank, ControBank)
admin.site.register(models.CardInfo, ControCardInfo)
admin.site.register(models.Auther, ControAuther)
admin.site.register(models.Book, ControBook)

admin.site.site_header = 'xx 项目管理系统'
admin.site.site_title = '登录系统后台'
admin.site.index_title = '后台管理'
