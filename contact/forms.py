from django import forms


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
            'placeholder': 'نام و نام خانوادگی'
        }))
    subject = forms.CharField(
        label='موضوع',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام و نام خانوادگی'
        })
    )
    phone = forms.IntegerField(
        label='شماره تماس',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام و نام خانوادگی'
        })
    )
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام و نام خانوادگی'
        })
    )

