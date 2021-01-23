from django.urls import path
from . import views
app_name = 'App_Quiz'

urlpatterns = [
    path('',views.teacher_home, name='teacher_home'),
    # path('create_quiz/',views.create_quiz.as_view(), name='create_quiz'),
]
