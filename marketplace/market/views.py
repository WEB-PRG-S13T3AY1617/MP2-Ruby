# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate, get_user_model, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from .forms import UserLoginForm, UserRegisterForm
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

def login_view(request):
    print(request.user.is_authenticated())
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request,user)
        return redirect("/market/")
    return render(request, "login.html", {"form":form, "title":title})

def register_view(request):
    print(request.user.is_authenticated())
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request,new_user)
        return redirect("/market/")
    context = {
        "form": form,
        "title": title
    }
    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    return redirect("/market/")
