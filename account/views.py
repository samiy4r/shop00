from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .forms import RegisterForm
from .models import User
from django.utils.crypto import get_random_string
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


def login(request):
    
    return render(request, 'login.html')


def activateAccount(request, activate_code):
    user = User.objects.filter(email_active_code__iexact=activate_code)
    user.email_active_code = get_random_string(80)
    user.is_active = True
    # TODO: show message in login that your account is activated
    return redirect(reverse('account:login'))