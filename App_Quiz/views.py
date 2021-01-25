from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout,authenticate
from App_Login.models import User, user_type
from App_Articles.models import Article
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from App_Quiz.models import QuizName,QuizQuestion,QuizTaker
# Create your views here.

def teacher_home(request):
    articles =Article.objects.all()
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_teach:
        # return HttpResponse("teacher")
        return render(request, 'App_Teacher/tc_home.html', context={'articles':articles})
    else:
        return redirect('App_Login:login_user')


class create_quiz(LoginRequiredMixin, CreateView):
    model = QuizName
    template_name = 'App_Teacher/create_quiz.html'
    fields = ('quiz_name',)
    def form_valid(self, form):
        quiz_obj = form.save(commit=False)
        quiz_obj.quiz_creator = self.request.user
        quiz_obj.is_published = False
        quiz_obj.save()
        user_type_obj = user_type.objects.get(user=self.request.user)
        if user_type_obj.is_teach:
            return redirect('App_Quiz:create_quiz')
        elif user_type_obj.is_student:
            return redirect('student_home')
