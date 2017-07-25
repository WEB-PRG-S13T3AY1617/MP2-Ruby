# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from .models import User, Post

# Create your views here.

def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:10]
    
    #relative path siya, okay? :) not absolute bes
    
    context = { 
        # context is a dictionary
        # to map the variables in the views and in the 
        # template (index.html)
        'latest_posts': latest_post_list,
    }
    return render(request, 'market/homepage.html', context)

def user(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:10]
    
    #relative path siya, okay? :) not absolute bes
    
    context = { 
        # context is a dictionary
        # to map the variables in the views and in the 
        # template (index.html)
        'latest_posts': latest_post_list,
    }
    return render(request, 'market/userprofile.html', context)

def postanitem(request):
    return render(request, 'market/post_item.html')
    