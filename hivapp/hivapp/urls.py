"""hivapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from hiv import views

urlpatterns = [
    #url(r'^wx/', admin.site.urls),
    url(r'^auth/user/api/rd3',views.renderTemplate.get_rd3_userinfo, name='rd3'),
    url(r'^weixin/login/?action=post_code',views.renderTemplate.getcode, name='code'),
    url(r'^pulics/login',views.renderTemplate.login, name='login'),
    url(r'^pulics/time', views.renderTemplate.GenerateTime, name='time'),
    url(r'^publics/place',views.renderTemplate.GenetePlace, name='place'),
    url(r'^auth/user/chat_room',views.renderTemplate.chat_room, name='chat_room'),
    url(r'^auth/user/me',views.renderTemplate.me, name='me'),
]