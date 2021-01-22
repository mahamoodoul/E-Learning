from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout,authenticate
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from App_Login.models import User, user_type
from django.contrib.auth.decorators import login_required
# from .models import
# Create your views here.


def register(request):
    return render(request,'App_Login/register.html')


def register_user(request):
    if (request.method == 'POST'):
        email = request.POST.get('email')
        password = request.POST.get('password')
        type_user = request.POST.get('user_type')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        print("hello")
        print(user_type)
        user = User.objects.create_user(
            email=email,
        )
        user.set_password(password)
        user.save()

        usert = None
        if type_user == 'student':
            usert = user_type(user=user,is_student=True,first_name=first_name, last_name=last_name)
        elif type_user == 'teacher':
            usert = user_type(user=user,is_teach=True,first_name=first_name, last_name=last_name)
        usert.save()
        #Successfully registered. Redirect to homepage
        # return HttpResponse("registered")
        return redirect('App_Login:login_user')
    return render(request, 'App_Login/register.html')


def login_user(request):
    if (request.method == 'POST'):
        email = request.POST.get('email') #Get email value from form
        password = request.POST.get('password') #Get password value from form
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            type_obj = user_type.objects.get(user=user)
            if user.is_authenticated and type_obj.is_student:
                return redirect('student_home') #Go to student home
            elif user.is_authenticated and type_obj.is_teach:
                return redirect('teacher_home')
                # return redirect('teacher_home') #Go to teacher home
        else:

            # Invalid email or password. Handle as you wish
            return redirect('register')
    return render(request, 'App_Login/login.html')

@login_required
def logout_user(request):
    logout(request)
    messages.warning(request, "You are logged out!!")
    # return HttpResponse("Loged out")
    return HttpResponseRedirect(reverse('App_Login:login_user'))
