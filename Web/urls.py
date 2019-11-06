from django.contrib.auth import views as auth_views

from django.contrib import admin
from django.urls import path, include, re_path
from app.views import show_content, show_article, create_user, login_user, add_comment, logout_user, add_content

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_user/', create_user),
    path('login/', login_user),
    path('logout/', logout_user),
    re_path(r'^add_comment_(?P<article_id>\d+)/$', add_comment),
    re_path(r'^(?P<article_id>\d+)/$', show_article),
    re_path(r'^(?P<q>\w+)/$', show_content)


]
