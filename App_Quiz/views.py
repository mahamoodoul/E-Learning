from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout,authenticate
from App_Login.models import User, user_type
from App_Articles.models import Article
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def teacher_home(request):
    articles =Article.objects.all()
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_teach:
        # return HttpResponse("teacher")
        return render(request, 'App_Teacher/tc_home.html', context={'articles':articles})
    else:
        return redirect('App_Login:login_user')
