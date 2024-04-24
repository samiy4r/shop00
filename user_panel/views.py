from django.shortcuts import render,redirect
from account.models import User
from .forms import PersonalForm
# Create your views here.
def profile_info (request):
       info = User.objects.filter(email__iexact = 'sami000@gmail.com')
       return render(request,'profile-personal-info.html',{'info':info})
       
def profile_edit (request):
       form = PersonalForm()
       if request.method == 'POST':
              form = PersonalForm(request.POST)
              if form.is_valid:
                     form.save
                     form = PersonalForm()
                     return render(request,'profile-additional-info.html',{form : 'form'})
       else:
              return render(request,'profile-additional-info.html',{form : 'form'})

       