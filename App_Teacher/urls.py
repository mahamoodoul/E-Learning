from django.urls import path
from . import views
app_name = 'App_Teacher'

urlpatterns = [
    path('',views.teacher_home, name='teacher_home'),
]
