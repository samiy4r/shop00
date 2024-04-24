from django import forms
from django.core.exceptions import ValidationError

class ForgetPassForm(forms.Form):
    password = forms.CharField(
        label= "رمز عبور",
        widget=forms.PasswordInput(attrs={
            'class': 'input-ui pr-2',
            "placeholder" : "رمز عبور خود را وارد کنید"
        })
    )
    confirm_password = forms.CharField(
        label="تکرار رمز عبور",
        widget=forms.PasswordInput(attrs={
            'class': "input-ui pr-2",
            "placeholder" : "رمز را تکرار کنید"
        })
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('رمز عبور و تکرار آن باهم تطابق ندارد')
        else:
            return confirm_password


class EmailForm(forms.Form):
        email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'class':'input-ui pr-2',
            "placeholder" : "ایمیل خود را وارد کنید"
        })
    )
class RegisterForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'class':'input-ui pr-2',
            "placeholder" : "ایمیل خود را وارد کنید"
        })
    )
    username = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(
            attrs = {
            'class': 'input-ui pr-2',
            'placeholder': 'نام کاربری خود را وارد کنید'
            }
        )
    )
    password = forms.CharField(
        error_messages={
               "min_length" : "رمز عبور کوتاه است"
                },
        max_length=55,
        min_length=8,
        label= "رمز عبور",
        widget=forms.PasswordInput(attrs={
            'class': 'input-ui pr-2',
            "placeholder" : "رمز عبور خود را وارد کنید"
        })
    )
    confirm_password = forms.CharField(
        label="تکرار رمز عبور",
        widget=forms.PasswordInput(attrs={
            'class': "input-ui pr-2",
            "placeholder" : "رمز را تکرار کنید"
        })
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('رمز عبور و تکرار آن باهم تطابق ندارد')
        else:
            return confirm_password
    

class LoginForm(forms.Form):
    email = forms.EmailField(
        label="ایمیل خود را وارد کنید",
        widget=forms.EmailInput(attrs={
            'class':'input-ui pr-2',
            
        })
    )
    password = forms.CharField(
        error_messages={
               'required': 'رمز عبور را وارد کنید'
                },
        label= "رمز عبور خود را وارد کنید",
        widget=forms.PasswordInput(attrs={
            'class': 'input-ui pr-2',
        
        })
    )
