from django.urls import path
from . import views
app_name = 'App_Quiz'

urlpatterns = [
    path('',views.teacher_home, name='teacher_home'),
    path('create_quiz/',views.create_quiz.as_view(), name='create_quiz'),
    path('quiz_list/',views.quiz_list, name='quiz_list'),
    path('total_questions/<quiz_name>/<quiz_id>',views.total_questions, name='total_questions'),
    path('publish_quiz/<quiz_id>',views.publish_quiz, name='publish_quiz'),




]
