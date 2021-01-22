from django.urls import path
from . import views
app_name = 'App_Login'



urlpatterns = [

    path('',views.register, name='register'),
    path('register_user/',views.register_user, name='register_user'),
    path('login_user/',views.login_user, name='login_user'),
    path('logout',views.logout_user, name='logout')
]
