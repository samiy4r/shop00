from django.shortcuts import render , HttpResponseRedirect 
from django.urls import reverse
from .models import ContactUs
from .forms import ContactForm

def contact(request):
    form = ContactForm(request.POST)
    if request.method == "POST":
        print(form.is_valid())
        print(form.cleaned_data)
    return render(request,'contact/index.html', {'form':ContactForm})



def add(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        Cform  = ContactUs(full_name=full_name , subject=subject , message=message , phone=phone , email=email)
        Cform.save()
    return HttpResponseRedirect(reverse("lightshop:contact"))
