from django.shortcuts import render, HttpResponseRedirect, HttpResponse, reverse, redirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from App_Articles.models import Article, Category, Comment
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from App_Articles.forms import CommentForm
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
