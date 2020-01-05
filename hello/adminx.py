import xadmin
# from django.contrib import admin
from hello import models
from hello.models import User, Person
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side, Field
from .models import Student, Card, FileImage
from xadmin import views
from .adminx_actions import ClearAction

# 全局设置,最好放到adminx.py开头位置
class GlobalSettings(object):
    site_title = "开发平台"  # title内容
    site_footer = "haha"  # 底部&后面
    menu_style = "accordion"  # 菜单折叠

    # 自定义菜单
    def get_site_menu(self):
        return [
            {
                'title': '自定义菜单',
                'icon': 'fa fa-bars',  # Font Awesome图标
                'menus': (
                    {
                      'title': 'Card表',
                      'icon': 'fa fa-bug',
                      'url': self.get_model_url(Card, 'changelist')
                    },
                    {
                        'title': 'a发邮件',
                        'icon': 'fa fa-envelope-o',
                        'url': self.get_model_url(Student, 'changelist')
                    }
                )
            },
            {
                'title': 'Bug统计',
                'icon': 'fa fa-bug',
                'menus':(
                    {
                        'title': 'Bug表',
                        'icon': 'fa fa-bug',
                        'url': "https://www.cnblogs.com/yoyoketang/"  # 自定义跳转列表
                    },
                )
            }
        ]

class ThemeStting(object):
    '''主题设置'''
    enable_themes = True  # 使用主题
    use_bootswatch = True  # bootswatch是一款基于bootstrap的汇集了多种风格的前端UI解决方案

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

    actions = [ClearAction, ]

class ControActicl(object):
    list_display = ['title', 'body', 'auth']

class MoreActicl(object):
    list_display = ['title', 'body', 'auth']

    readonly_fields = ['detail']  # 只读字段

    exclude = ['auth']  # 不显示某个字段

    # layout布局
    form_layout = (
        Fieldset(u'',
            Row('title', 'auth'),  # Row 表示将里面的字段作为一行显示
            Row('classify'),
            css_class = 'unsort'  # 不让区块拖动
            ),
        Fieldset('正文内容',  # Fieldset第一个参数表示区块名称
            'body',
            css_class = 'unsort no_title'  # 不让区块拖动, 不显示区块名称
        ),
        # Fieldset('备注',
        #          Row('detail'),
        #          ),
        TabHolder(
            Tab('body-raw',
                Field('title', css_class="extra"
                      ),
                Field('body'),
                css_class='unsort',
                ),
            Tab('body-json',
                Field('body',
                      ),
                css_class='unsort',
                )
        )
    )

# class ControlStudent(object):
#     # 显示的字段
#     list_display = ['student_id', 'name', 'age',]
#     # 搜索条件
#     search_fields = ('name',)
#     # 每页显示10条
#     list_per_page = 10
#     actions = [ClearAction, ]

class ControlFiles(object):
    list_display = ['title', 'add_time']

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
xadmin.site.register(models.ArticleDetail, MoreActicl)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, ThemeStting)
# xadmin.site.register(Student, ControlStudent)
xadmin.site.register(FileImage, ControlFiles)

xadmin.site.site_header = 'xx 项目管理系统'
xadmin.site.site_title = '登录系统后台'
xadmin.site.index_title = '后台管理'
