from django import forms
from account.models import User

class PersonalForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'phone', 'id_number', 'cart_number']
        labels = {
            'name': 'نام  ‍',
            'last_name':'خانوادگی',
            'phone': 'شماره تماس',
            'email': 'ایمیل',
            'id_number': 'کد ملی',
            'cart_number': 'شماره کارت ',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'input-ui pl-2',
        }),
            'last_name': forms.TextInput(attrs={
                'class': 'input-ui pl-2',
        }),
            'phone': forms.TextInput(attrs={
                'class': 'input-ui pl-2',
        }),
            'id_number': forms.TextInput(attrs={
                'class': 'input-ui pl-2',
        }),
            'cart_number': forms.TextInput(attrs={
                'class': 'input-ui pl-2',
        }),
            'email':forms.TextInput(attrs={
                'class': 'input-ui pl-2',
        })
        }
