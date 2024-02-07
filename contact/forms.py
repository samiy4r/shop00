from django import forms
from .models import ContactUs


class ContactForm(forms.Form):
    full_name = forms.CharField(
        label='نام شما',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام و نام خانوادگی'
        })
    )
    message = forms.CharField(
        label='پیام',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'پیام'
        }))
    subject = forms.CharField(
        label='موضوع',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'موضوع'
        })
    )
    phone = forms.IntegerField(
        label='شماره تماس',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'شماره تماس'
        })
    )
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'ایمیل'
        })
    )

class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'phone', 'subject', 'message']
        labels = {
            'full_name': 'نام و نام خانوادگی ‍',
            'phone': 'شماره تماس',
            'email': 'ایمیل',
            'subject': 'موضوع',
            'message': 'پیام شما'
        }
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
        }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
        }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
        }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
        }),
            'email':forms.TextInput(attrs={
                'class': 'form-control',
        })
        }
        error_messages = {
            'full_name': {
                'required': 'نام و نام خانوادگی اجباری میباشد لطفا وارد کنید'
            }
        }
