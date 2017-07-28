from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth import views

#from marketplace.core import views as core_views

from . import views
from market.views import (login_view, register_view, logout_view, postanitem)

app_name = 'market'

urlpatterns = [
    url(r'^$', views.index, name='index'), #shows what is inside views.py   
    url(r'^postanitem/$', views.postanitem, name='postanitem'),
    url(r'^(?P<user_id>[0-9]+)/user/$', views.user, name='user'),
    url(r'^(?P<post_id>[0-9]+)/itemdetail/$', views.itemdetail, name='itemdetail'),
]
