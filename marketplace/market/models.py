# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

def upload_location(instance, filename):
    return "%s/%s" %(instance.id,filename)

class Profile(models.Model):
    user = models.ForeignKey(User, primary_key=True,  related_name='profile', on_delete=models.CASCADE)
    Degree_Program_or_Office = models.CharField(max_length=50)
    Professional = 'Professional'
    Student = 'Student'
    TYPES_USER = (
        (Student, 'Student'),
        (Professional, 'Professional'),
    )
    usertypes = models.CharField(max_length=12,choices=TYPES_USER,default=Student)
    
    def __str__(self):
        return str(self.user)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    itemname = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    condition = models.CharField(max_length=200)
    # remove photos from inside 
    tb_img = models.ImageField(upload_to = upload_location, 
                               null=True, 
                               blank=True,
                               width_field = "width_field",
                               height_field = "height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    tag = models.CharField(max_length = 50)
    pub_date = models.DateTimeField(auto_now_add = True)
    Office = 'Office'
    Academic = 'Academic'
    TYPES_POST = (
        (Office, 'Office'),
        (Academic, 'Academic'),
    )
    posttypes = models.CharField(max_length=9,choices=TYPES_POST,default=Office)
    coursename = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.itemname
    
    def me(self):
        return self.condition.replace('-',' ')

class Offer(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Exchange = 'Exchange'
    Purchase = 'Purchase'
    TYPES_OFFER = (
        (Exchange, 'Exchange'),
        (Purchase, 'Purchase'),
    )
    offertypes = models.CharField(max_length=9,choices=TYPES_OFFER,default=Exchange)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null = True, blank = True)
    status = models.IntegerField(default=0)
    
    def __str__(self):
        return self.post.itemname + " made by " + self.user.username

# Create your models here.
