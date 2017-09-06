from django.shortcuts import render, redirect
from django.contrib import messages
from ..log_reg.models import User
from .models import *
from django.core.urlresolvers import reverse

def index(request):
    if not 'user_name' in request.session:
        messages.add_message(request, messages.INFO, "Must be logged in to view this page")
        return redirect('log_reg:index')
    context = {
        'cats':Cat.objects.all(),
        'logged_user':User.objects.get(id = request.session['user_id']),
    }
    return render(request, "cats/index.html", context)

def logout(request):
    request.session.flush()
    return redirect('log_reg:index')

def add(request):
    if not 'user_name' in request.session:
        messages.add_message(request, messages.INFO, "Must be logged in to view this page")
        return redirect('log_reg:index')
    return render(request, "cats/add.html")

def create_cat(request):
    if request.method == "POST":
        result = Cat.objects.create_cat(request.POST)
        if result[0] == False:
            context = {'error':result[1]}
            return render(request, "cats/add.html", context)
        if result[0] == True:
            return redirect('cats:index')

def add_like(request, user_id, cat_id):
    like = Like.objects.add_like(user_id, cat_id)
    if like == True:
        return redirect('cats:index')

def show(request, cat_id):
    if not 'user_name' in request.session:
        messages.add_message(request, messages.INFO, "Must be logged in to view this page")
        return redirect('log_reg:index')
    result = Cat.objects.get(id = cat_id)
    likes = Like.objects.filter(cat = result)
    likes_count = len(likes)
    context = {
        'cat':result,
        'likes_count':likes_count
    }
    return render(request, "cats/show.html", context)

def delete(request, cat_id):
    Cat.objects.delete_cat(cat_id)
    return redirect('cats:index')

def update(request, cat_id):
    if not 'user_name' in request.session:
        messages.add_message(request, messages.INFO, "Must be logged in to view this page")
        return redirect('log_reg:index')
    context = {
        'cat_id':cat_id,
    }
    return render(request, "cats/update.html", context)

def edit(request):
    if request.method == "POST":
        result = Cat.objects.edit_cat(request.POST)
        if result[0] == False:
            context = {'error':result[1]}
            return render(request, "cats/update.html", context)
        if result[0] == True:
            return redirect('cats:index')

# Create your views here.
