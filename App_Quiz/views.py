from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect,reverse
from django.contrib.auth import login, logout,authenticate
from App_Login.models import User, user_type
from App_Articles.models import Article
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from App_Quiz.models import QuizName,QuizQuestion,QuizTaker
from App_Quiz.forms import CreateQuizForm
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


@login_required
def quiz_list(request):
    all_quiz_name = QuizName.objects.all()
    current_user = request.user
    form = CreateQuizForm(instance=current_user)

    if request.method == 'POST':
        form_data = CreateQuizForm(data=request.POST)
        if form_data.is_valid():
            user_type_obj = user_type.objects.get(user=request.user)
            if user_type_obj.is_teach:
                data_question = form_data.save(commit=False)
                data_question.question_creator = request.user
                data_question.save()
                return HttpResponseRedirect(reverse('App_Quiz:quiz_list'))
    return render(request,'App_Teacher/quiz_list.html', context={'all_quiz_name':all_quiz_name, 'form':form})

@login_required
def  total_questions(request, quiz_id, quiz_name):
    quiz_info = QuizQuestion.objects.filter(quiz_name = quiz_id)
    quiz_name_obj = QuizName.objects.get(pk=quiz_id)
    total_questions = quiz_info.count()
    return render(request, 'App_Teacher/quiz_info.html', context={'total_questions': total_questions, 'quiz_info': quiz_info,'quiz_name':quiz_name, 'quiz_id':quiz_id,'quiz_name_obj':quiz_name_obj})


@login_required
def publish_quiz(request, quiz_id):
    QuizName.objects.filter(pk=quiz_id).update(	is_published=True)
    return HttpResponseRedirect(reverse('App_Quiz:quiz_list'))
