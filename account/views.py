from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegisterForm, LoginForm
from .models import User
from django.utils.crypto import get_random_string
from django.contrib.auth import login, logout
# Create your views here.

def register(request):
    form = RegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user_email = request.POST.get('email')
            user = User.objects.filter(email__iexact=user_email).exists()
            if user:
                form.add_error('email', 'این ایمیل قبلا ثبت نام کرده است')
                return render(request, 'register.html', {"form": form})
            else:
                user_pass = form.cleaned_data.get('passowrd')
                new_user = User(email=user_email, is_active=False, username=user_email)
                new_user.set_password(user_pass)
                new_user.email_active_code = get_random_string(80)
                new_user.save()
                # TODO: 
                return redirect(reverse('account:login'))

        else:
            return render(request, 'register.html', {"form": form})

    return render(request, 'register.html', {"form": RegisterForm})


def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user_email = request.POST.get('email')
            user = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if user.is_active:
                    user_password = request.POST.get('password')
                    is_password_correct = user.check_password(user_password)
                    if is_password_correct:
                        print(request.POST)
                        login(request, user)
                        return HttpResponseRedirect(reverse('shop:index'))
        else:
            return render(request, 'login.html', {'form': form})

    return render(request, 'login.html', {'form': LoginForm})


def activateAccount(request, activate_code):
    user = User.objects.filter(email_active_code__iexact=activate_code).first()
    if user is not None:
        user.email_active_code = get_random_string(80)
        user.is_active = True
        user.save()
        return render(request, 'login.html', {'message':'اکانت شما فعال شد'})
    else:
        return render(request, 'login.html', {'message':'اکانت شما پیدا نشد'})
