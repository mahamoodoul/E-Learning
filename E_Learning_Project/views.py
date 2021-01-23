from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect
from django.views.generic import ListView
from App_Articles.models import Article
# Create your views here.

def student_home(request):
    return HttpResponseRedirect(reverse('App_Student:student_home'))

def teacher_home(request):
    return HttpResponseRedirect(reverse('App_Quiz:teacher_home'))

class article_list(ListView):
    context_object_name = 'articles'
    model = Article
    template_name = 'App_Teacher/tc_home.html'
