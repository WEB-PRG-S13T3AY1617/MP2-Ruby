# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

def upload_location(instance, filename):
    return "%s/%s" %(instance.id,filename)

#class UserExtend(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    Degree_Program_or_Office = models.CharField(max_length=50, blank=True)
#    Professional = 'Professional'
#    Student = 'Student'
#    TYPES_CHOICES = (
#        (Student, 'Student'),
#        (Professional, 'Professional'),
#    )
#    types = models.CharField(max_length=12,choices=TYPES_CHOICES,default=Student,)
#    
#    def __str__(self):
#        return self.Degree_Program_or_Office

class Profile(models.Model):
    user = models.ForeignKey(User,  related_name='profile', on_delete=models.CASCADE)
    Degree_Program_or_Office = models.CharField(max_length=50)
    Professional = 'Professional'
    Student = 'Student'
    TYPES_CHOICES = (
        (Student, 'Student'),
        (Professional, 'Professional'),
    )
    types = models.CharField(max_length=12,choices=TYPES_CHOICES,default=Student)
    
    def __str__(self):
        return str(self.user)
    
#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        Profile.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()

    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    itemname = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    condition = models.CharField(max_length=200)
    Usertypes = models.CharField(max_length=50)
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
    
    def __str__(self):
        return self.itemname
    

# Create your models here.
