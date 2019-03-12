"""ReaperEngine_prj URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from ReaperEngine_app import views as ReaperEngine_views
from accounts_app import views as accounts_views
from support_app import views as support_views
from blog_app import views as blog_views
from donations_app import views as donations_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ReaperEngine_views.home, name='home'),
    url(r'^donations$', donations_views.donations, name='donations'),
    url(r'^blog$', blog_views.post_list, name='blog'),
    url(r'^post/new/$', blog_views.new_post, name='new_post'),
    url(r'^blog/(?P<id>\d+)/$', blog_views.post_detail, name='post_detail'),
    url(r'^blog/(?P<id>\d+)/edit$', blog_views.edit_post, name='edit'),
    url(r'^support/$', support_views.support, name='support'),
    url(r'^support/vote/(?P<id>\d+)$', support_views.vote, name='vote'),
    url(r'^support/comment/(?P<id>\d+)$', support_views.comment, name='comment'),
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),
]
