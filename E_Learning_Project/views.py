from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect

# Create your views here.

def student_home(request):
    return HttpResponseRedirect(reverse('App_Student:student_home'))

def teacher_home(request):
    return HttpResponseRedirect(reverse('App_Teacher:teacher_home'))
