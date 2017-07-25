# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import views
from django.contrib import admin

# Register your models here.

from models import *

admin.site.register(User)
admin.site.register(Post)
