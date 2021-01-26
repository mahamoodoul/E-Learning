from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect,reverse
from django.contrib.auth import login, logout,authenticate
from App_Login.models import User, user_type
from App_Articles.models import Article
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from App_Quiz.models import QuizName,QuizQuestion,QuizTaker
from django.core.paginator import Paginator
from django.http import JsonResponse




print(" heloo shakil")

def student_home(request):
    articles =Article.objects.all()
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_student:
        return render(request,'App_Student/st_home.html', context={'articles':articles})
    else:
        return redirect('App_Login:login_user')

@login_required
def attempt_quiz(request):
    available_quiz = QuizName.objects.filter(is_published = True)
    return render(request, 'App_Student/attempt_quiz.html', context={'available_quiz': available_quiz})


@login_required
def quiz_running(request, quiz_name, quiz_id):
    obj = QuizQuestion.objects.filter(quiz_name = quiz_id)
    count = QuizQuestion.objects.filter(quiz_name = quiz_id).count()
    request.session['quiz_id'] = quiz_id
    paginator = Paginator(obj,1)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page =1
    try:
        questions = paginator.page(page)
    except(EmptyPage,InvalidPage):

        questions=paginator.page(paginator.num_pages)

    return render(request,'App_Student/quiz_running.html',{'obj':obj,'questions':questions,'count':count})


def result(request):
    quiz_id = request.session['quiz_id']
    obj = QuizQuestion.objects.filter(quiz_name = quiz_id)
    correct_answer = []
    for i in obj:
        correct_answer.append(i.answer)
    score =0
    ans_list = request.session['ans_list']

    print(f"your ans list from result page :{request.session['ans_list']}")
    print(f"your score list: {len(ans_list)}")
    del request.session['ans_list']
    print(f"your ans list from result page :{ans_list}")
    total_correct_ans= {}
    i = 0
    for key, value in ans_list.items():
        correct_ans = QuizQuestion.objects.filter(pk=key).filter(answer=value)
        total_correct_ans[i] = correct_ans
        i=i+1
        print (key, value)
    print(total_correct_ans)
    print(len(total_correct_ans))
    return render(request,'App_Student/result.html',context={'score':len(total_correct_ans),'lst':ans_list})

ans_list ={}
answer_list =[]
def save_ans(request):
    ans = request.GET['ans']
    question_id = request.GET['question_id']
    print(question_id)
    print(f"you selected: {ans}")
    ans_list[question_id] = ans
    request.session['ans_list'] = ans_list
    print(f"you list of correct answer: {request.session['ans_list']}")
    return JsonResponse({'lst':ans_list}, status = 200)
