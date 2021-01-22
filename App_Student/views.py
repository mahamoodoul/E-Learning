from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout,authenticate
from App_Login.models import User, user_type
# Create your views here.


def student_home(request):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_student:
        return HttpResponse("heelo")
        return render(request,'App_Student/st_home.html')
    else:
        return redirect('App_Login:login_user')
