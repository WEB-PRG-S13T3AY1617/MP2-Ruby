# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate, get_user_model, logout
from django.shortcuts import render, render_to_response , get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import UserLoginForm, UserForm, PostForm, ProfileForm, OfferForm
from .models import User, Post, Offer, Profile

# Create your views here.

def index(request):
    
    latest_post_list = Post.objects.order_by('-pub_date')

    request.session['paginate_by'] = 10
    
    if request.GET and ('paginate_by' in request.session or 'paginate_by' in request.get):

        if request.session['paginate_by'] != int(request.GET.get('paginate_by', 10)):
            request.session['paginate_by'] = int(request.GET.get('paginate_by', 10))
        
    if 'paginate_by' in request.session:
        m = request.session['paginate_by']
    else: 
        m = 10
    
    paginator = Paginator(latest_post_list, m) # Show 10 posts per page

    page = request.GET.get('page')

    try:
        latest_post_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        latest_post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        latest_post_list = paginator.page(paginator.num_pages)
    context = { 
        'latest_posts': latest_post_list,
        'paginate_by': m,
    }
    return render(request, 'market/homepage.html', context)

def user(request, user_id):
    user2 =get_object_or_404(User,pk=user_id)
    userprof = get_object_or_404(Profile,pk=user_id)
    latest_post_list = Post.objects.filter(user_id=user_id).order_by('-pub_date')[:10]
    list_offer = Offer.objects.order_by('-pub_date')
    offerobj = None
    oid = None
    if request.method == 'GET':
        oid = request.GET.get('offerid')
        print(oid)
    if oid != None:
        offerobj = get_object_or_404(Offer,pk=oid)
        
    m = 10  
    paginator = Paginator(latest_post_list, m) # Show 10 posts per page

    page = request.GET.get('page')

    try:
        latest_post_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        latest_post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        latest_post_list = paginator.page(paginator.num_pages)
    context = { 
        'user2':user2,
        'userprof':userprof,
        'latest_posts': latest_post_list,
        'list_offer':list_offer,
        'offerobj':offerobj,
    }
    return render(request, 'market/userprofile.html', context)
def accept(request, offer_id):
    print("Accept")
    offerobj = get_object_or_404(Offer,pk=offer_id)
    postobj = get_object_or_404(Post,pk= offerobj.post.id)
    #owner_id = offerobj.post.user.id
    user_id = offerobj.post.user.id
    
    buyer_id = offerobj.user.id
    buyerobj = get_object_or_404(User,pk= buyer_id)
    offerobj.post.user = buyerobj
    offerobj.post.save()
    
    if request.method == 'POST':
        reason = request.POST['reason']
        print(reason+"hello")
        offerobj.reason = reason
        offerobj.save()
    
    offerobj.status = 1
    offerobj.save()
    return user(request, user_id)
    
def decline(request, offer_id):
    print("Decline")
    offerobj = get_object_or_404(Offer,pk=offer_id)
    user_id = offerobj.post.user.id
    if request.method == 'POST':
        reason = request.POST['reason']
        print(reason+"hello")
        offerobj.reason = reason
        offerobj.save()
    offerobj.status = 2
    offerobj.save()
    return user(request, user_id)
    
    
def postanitem(request):
    if request.user.is_authenticated():
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            # message success
            return redirect("/market/")
        context = {
            "form": form,
        }
        return render(request, "market/post_item.html", context)
    else:
        return index(request)

def itemdetail(request, post_id):
    post =get_object_or_404(Post,pk=post_id)
    user2 = get_object_or_404(User,pk=post.user.id)
   
    form = OfferForm(request.POST or None)
    if form.is_valid():
        that = form.save(commit=False)
        that.user = request.user
        that.save()
        return redirect('market/itemdetail.html')
    context = { 
        'user2':user2,
        'post': post,
        'form': form,
    }
    return render(request, 'market/itemdetail.html', context)

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
    title = "Registration Part 1"
    form = UserForm(request.POST or None)
    if form.is_valid():
        Auser = form.save(commit=False)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        Auser.set_password(password)
        Auser.save()
        new_user = authenticate(username=Auser.username, password=password)
        login(request,new_user)
        return redirect("/aregister/")
    context = {
        "form": form,
        "title": title
    }
    return render(request, "login.html", context)

def register(request):
    print(request.user.is_authenticated())
    title = "Registration Part 2"
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        that = form.save(commit=False)
        that.user = request.user
        that.save()
        return redirect("/market/")
    context = {
        "this": form,
        "title": title
    }
    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    return redirect("/market/")

def searchpic(request):
    query = request.GET.get('tag')
    latest_post_list = Post.objects.filter(tag=query).order_by('-pub_date')
    
    page = request.GET.get('page1', 1)
    paginator = Paginator(latest_post_list, 10) # Show 10 pics per page

    try:
        latest_post_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        latest_post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        latest_post_list = paginator.page(paginator.num_pages)
    context = { 
        'latest_posts': latest_post_list,
    }
    
   
    return render(request, 'market/search_results.html', context)

def searchtag(request, post_tag):
    latest_post_list = Post.objects.filter(tag=post_tag).order_by('-pub_date')
    
    m = 10
    
    if request.GET:
        m = request.GET.get('paginate_by', 10)
    
    paginator = Paginator(latest_post_list, m) # Show 10 posts per page

    page = request.GET.get('page')

    try:
        latest_post_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        latest_post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        latest_post_list = paginator.page(paginator.num_pages)
    context = { 
        'latest_posts': latest_post_list,
    }
    return render(request, 'market/homepage.html', context)
def searchcondition(request, post_condition):
    latest_post_list = Post.objects.filter(condition=post_condition).order_by('-pub_date')
    m = 10
    
    if request.GET:
        m = request.GET.get('paginate_by', 10)
    
    paginator = Paginator(latest_post_list, m) # Show 10 posts per page

    page = request.GET.get('page')

    try:
        latest_post_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        latest_post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        latest_post_list = paginator.page(paginator.num_pages)
    context = { 
        'latest_posts': latest_post_list,
    }
    return render(request, 'market/homepage.html', context)
def searchtype(request, post_type):
    latest_post_list = Post.objects.filter(posttypes=post_type).order_by('-pub_date')
    
    m = 10
    
    if request.GET:
        m = request.GET.get('paginate_by', 10)
    
    paginator = Paginator(latest_post_list, m) # Show 10 posts per page

    page = request.GET.get('page')

    try:
        latest_post_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        latest_post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        latest_post_list = paginator.page(paginator.num_pages)
    context = { 
        'latest_posts': latest_post_list,
    }
    return render(request, 'market/homepage.html', context)
def searchcourse(request, post_course):
    latest_post_list = Post.objects.filter(coursename=post_course).order_by('-pub_date')
    
    m = 10
    
    if request.GET:
        m = request.GET.get('paginate_by', 10)
    
    paginator = Paginator(latest_post_list, m) # Show 10 posts per page

    page = request.GET.get('page')

    try:
        latest_post_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        latest_post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        latest_post_list = paginator.page(paginator.num_pages)
    context = { 
        'latest_posts': latest_post_list,
    }
    return render(request, 'market/homepage.html', context)


