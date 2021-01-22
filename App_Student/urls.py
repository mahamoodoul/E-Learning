from django.urls import path
from . import views
app_name = 'App_Student'

urlpatterns = [
    path('',views.student_home, name='student_home'),
]
