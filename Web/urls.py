from django.contrib.auth import views as auth_views

from django.contrib import admin
from django.urls import path, include, re_path
import app.views as views

urlpatterns = [
    path('add_content/', views.add_content),
    path('admin/', admin.site.urls),
    path('create_user/', views.create_user),
    path('login/', views.login_user),
    path('logout/', views.logout_user),
    re_path(r'^add_comment_(?P<article_id>\d+)/$', views.add_comment),
    re_path(r'^(?P<article_id>\d+)/$', views.show_article),
    re_path(r'^(?P<q>\w+)/$', views.sort_by_category),
    path('', views.main_page)

]
