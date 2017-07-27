from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth import views

#from marketplace.core import views as core_views

from . import views

app_name = 'market'

urlpatterns = [
    url(r'^$', views.index, name='index'), #shows what is inside views.py
    #url(r'^signup/$', core_views.signup, name='signup'),
    #url(r'^auth/$', views.auth_view, name='auth'),
    #url(r'^loggedin/$', views.loggedin, name='loggedin'),
    url(r'^login/$', auth_views.login, name='login'),   
    url(r'^user/$', views.user, name='user'),
    url(r'^postanitem/$', views.postanitem, name='postanitem'),
]

# S O M E  N O T E S : #######################
# "." (dot) means same package folder
# what are regular expressions?
# $ -> no value after
# / -> yes value after
# processing requests -- linear search for patterns
# ?P<variable> - name group