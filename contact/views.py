from django.shortcuts import render , HttpResponseRedirect 
from django.urls import reverse
from .models import ContactUs
from .forms import ContactUsModelForm

def contact(request):
    if request.method == "POST":
        form = ContactUsModelForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request,'contact/index.html', {'form':form})
    return render(request,'contact/index.html', {'form':ContactUsModelForm})
