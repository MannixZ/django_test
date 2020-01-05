"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import view, testdb, settings
from hello import views
import xadmin
from django.views.static import serve

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    url(r'^$', view.index),
    url(r'^hello$', view.hello),
    url('^demo/$', views.demo, name="demp_page"),
    url('^demo/page=(\d+)$', views.page),
    path(r"archive/<year>/<month>.html", views.home),
    url(r"^archive1/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2}).html$", views.home),
    url(r'^home/$', views.home1, name="home_page"),
    url(r'^yoyo/$', views.yoyo),
    url(r'^page1/$', views.page1),
    url(r'^chlid$', views.child),
    url(r'^testdb$', testdb.testdb),
    # url(r'^register$', testdb.add_user),
    url(r'^update$', testdb.update_psw),
    url(r'^delete$', testdb.delete_user),
    # url(r'^mail$', testdb.select_mail),
    url(r'^slec_all$', testdb.slec_all),
    url(r'^slec_filter$', testdb.sele_filter),
    url(r'^sele_values$', testdb.sele_values),
    url(r'^sele_get$', testdb.sele_get),
    url(r'^sele_first_last$', testdb.sele_first_last),
    url(r'^get_json$', testdb.get_json),
    url(r'^to_dict$', testdb.to_dict),
    url(r'^json_data$', testdb.json_data),
    url(r'^qq/$', views.test_qq),
    url(r'^result$', views.result_qq),
    url(r'^email$', views.user),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^reset/$', views.reset_psw),
    url(r'^mail$', views.mail),
    url(r'^mail_html$', views.mail_html),
    url(r'^file_mail$', views.file_mail),
    url(r'^file_html_mail$', views.file_html_mail),
    url(r'^login2/', views.loginView),
    url(r'^logout/', views.logoutView),
    url(r'^success/', views.successView),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]
