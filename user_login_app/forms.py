from .models import UserLogin
from django import forms
from django.forms import PasswordInput

class UserLoginForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = UserLogin
        widgets ={
            'password': PasswordInput(),
        }
        fields = '__all__'
        
    