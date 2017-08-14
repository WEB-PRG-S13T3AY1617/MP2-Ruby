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
    url(r'^searchpic/$', views.searchpic, name='searchpic'),
    url(r'^(?P<user_id>[0-9]+)/user/$', views.user, name='user'),
    url(r'^(?P<post_id>[0-9]+)/itemdetail/$', views.itemdetail, name='itemdetail'),
    url(r'^(?P<post_id>[0-9]+)/itemdetail/makeoffer$', views.makeoffer, name='makeoffer'),
    url(r'^(?P<post_tag>[-\w]+)/searchtag/$', views.searchtag, name='searchtag'),
    url(r'^(?P<post_type>[-\w]+)/searchtype/$', views.searchtype, name='searchtype'),
    url(r'^(?P<post_condition>.*)/searchcondition/$', views.searchcondition, name='searchcondition'),
    url(r'^(?P<post_course>[-\w]+)/searchcourse/$', views.searchcourse, name='searchcourse'),
    url(r'^(?P<offer_id>[0-9]+)/user/accept$', views.accept, name='accept'),
    url(r'^(?P<offer_id>[0-9]+)/user/decline$', views.decline, name='decline'),
    url(r'^(?P<offer_id>[0-9]+)/user/update$', views.update, name='update'),
    url(r'^(?P<offer_id>[0-9]+)/user/cancel$', views.cancel, name='cancel'),
   
    
]
