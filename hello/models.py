from django.db import models

# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=20)

class Person(models.Model):
    '''用户信息'''
    name = models.CharField(max_length=30)
    age = models.IntegerField

    def __str__(self):
        return self.__doc__ + ":name->" + self.name

class User(models.Model):
    '''注册表'''
    user_name = models.CharField(max_length=30,
                                 primary_key=True)
    psw = models.CharField(max_length=30)
    mail = models.CharField(max_length=30)

    def __str__(self):
        return self.__doc__ + ":user_name->" + self.user_name

class Article(models.Model):
    '''文章'''
    title = models.CharField(max_length=30, verbose_name='标题')  # 标题
    body = models.TextField(verbose_name='正文') # 正文
    auth = models.CharField(max_length=10, verbose_name='作者') # 作者
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')

    def __str__(self):
        return self.__doc__ + "title->" + self.title

    class Meta:
        verbose_name_plural = '文章列表'