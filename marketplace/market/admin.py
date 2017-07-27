# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#from .models import Profile
# Register your models here.

from models import *

admin.site.register(Post)

#class UserProfileInline(admin.StackedInline):
#    model = Profile
#    can_delete = False
#    verbose_name_plural = 'Profile'

#class UserAdmin(BaseUserAdmin):
#    inlines = (UserProfileInline, )
    
#admin.site.unregister(User)
#admin.site.register(User)
