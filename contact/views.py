from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    form = ContactForm(request.POST)
    if request.method == "POST":
        print(form.is_valid())
        print(form.cleaned_data)
    return render(request,'contact/index.html', {'form':ContactForm})
