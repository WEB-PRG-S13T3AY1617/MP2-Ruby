from django.conf.urls import url
from django.contrib.auth import views as auth_views
#from marketplace.core import views as core_views

from . import views

app_name = 'market'

urlpatterns = [
    url(r'^$', views.index, name='index'), #shows what is inside views.py
    #url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),   
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