# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from .models import User, Post

# Create your views here.

def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:10]
    
    context = { 
        'latest_posts': latest_post_list,
    }
    return render(request, 'market/homepage.html', context)

def user(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:10]
    
    context = {
        'latest_posts': latest_post_list,
    }
    return render(request, 'market/userprofile.html', context)

def postanitem(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    try:
        selected_post = user.post_set.get(pk=request.POST['post'])
    except (KeyError, Post.DoesNotExist):
        return render(request, 'market/postanitem.html', {
            'user': user,
            'error_message': "Invalid.",
        })
    else:
        selected_post.save()
        return HttpResponseRedirect(reverse('market:postanitem', args=(user.id,)))

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            name = form.cleaned_data.get('name')
            raw_password = form.cleaned_data.get('pw')
            numType = form.cleaned_data.get('numType')
            theType = form.cleaned_data.get('other')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/market')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    username=request.POST.get('username', '')
    password=request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/account/loggedin/")
    else:
        # Show an error page
        return HttpResponseRedirect("/account/invalid/")

#def login(request):
#    username = 'not_logged_in'
#    
#    if request.method == 'POST':
#        MyLoginForm = LoginForm(request.POST)
##    
#    if MyLoginForm.is_valid():
#        username = MyLoginForm.cleaned_data['username']
#        request.session['username'] = username
#    else:
#        MyLoginForm = LoginForm()
#        
#    return render(request, 'homepage.html', {'username' : username})

#def formView(request):
#    if request.session.has_key('username'):
#        username = request.session['username']
#        return render(request, 'homepage.html', {'username': username})
#    else:
#        return render(request, 'login.html', {})