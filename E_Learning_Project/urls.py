from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('App_Login.urls')),
    path('student/', include('App_Student.urls')),
    path('teacher/', include('App_Teacher.urls')),
    path('std_home',views.student_home, name='student_home'),
    path('tc_home',views.teacher_home, name='teacher_home'),
]
