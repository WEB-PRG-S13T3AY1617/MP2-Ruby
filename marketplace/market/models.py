# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models


#class User(models.Model):
#    username = models.CharField(max_length=50)
#    name = models.CharField(max_length=100)
#    password = models.CharField(max_length=15)
#    def __str__(self):
#        return self.name

#class Profile(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    types_place = models.CharField(max_length=50, blank=True)
#    types = models.IntegerField(default=0)
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, default='', blank=True)
    usertype = models.IntegerField(default=0,null=True, blank=True)#0-staff 1- student
    types_place = models.CharField(max_length=50, blank=True)#degreeprogram or office
    def __str__(self):
        return self.user.username
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender=User)
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    itemname = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    condition = models.CharField(max_length=200)
    Usertypes = models.CharField(max_length=50)
    degprog = models.CharField(max_length=200, default='none')
    # remove photos from inside 
    tb_img = models.CharField(max_length = 200)
    tag = models.CharField(max_length = 50)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.itemname
    

# Create your models here.
