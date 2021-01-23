from django.shortcuts import render, HttpResponseRedirect, HttpResponse, reverse, redirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from App_Articles.models import Article, Category, Comment, Question, AnswerQuestion
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from App_Articles.forms import CommentForm, AnswerForm
from App_Login.models import User, user_type
import uuid
# Create your views here.


class CreateArticles(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'App_Articles/create_articles.html'
    fields = ('articles_title','articles_category', 'articles_content', 'articles_image',)
    def form_valid(self, form):
        article_obj = form.save(commit=False)
        article_obj.author = self.request.user
        title = article_obj.articles_title
        article_obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        article_obj.save()
        user_type_obj = user_type.objects.get(user=self.request.user)
        if user_type_obj.is_student:
            return redirect('student_home') #Go to student home
        elif user_type_obj.is_teach:
            return redirect('teacher_home')


@login_required
def articale_details(request, slug):
    article = Article.objects.get(slug=slug)
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.article = article
            comment.save()
            return HttpResponseRedirect(reverse('App_Articles:article_details', kwargs={'slug':slug}))
    return render(request, 'App_Articles/article_details.html', context={'article':article, 'comment_form':comment_form })


class ask_question(LoginRequiredMixin, CreateView):
    model = Question
    template_name = 'App_Articles/ask_question.html'
    fields = ('question_title','question_content')
    def form_valid(self, form):
        qs_obj = form.save(commit=False)
        qs_obj.question_poster = self.request.user
        title = qs_obj.question_title
        qs_obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        qs_obj.save()
        user_type_obj = user_type.objects.get(user=self.request.user)
        if user_type_obj.is_student:
            return redirect('student_home')
        elif user_type_obj.is_teach:
            return redirect('teacher_home')


class question_list(ListView):
    context_object_name = 'questions'
    model = Question
    template_name = 'App_Articles/question_list.html'


@login_required
def answer_question(request, slug):
    question = Question.objects.get(slug=slug)
    ans_form = AnswerForm()
    if request.method == 'POST':
        ans_form = AnswerForm(request.POST)
        if ans_form.is_valid():
            ans = ans_form.save(commit=False)
            ans.user = request.user
            ans.question_answer = question
            ans.save()
            return HttpResponseRedirect(reverse('App_Articles:answer_question', kwargs={'slug':slug}))
    return render(request, 'App_Articles/answer_question.html', context={'question':question, 'ans_form':ans_form })
