from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


# Create your models here.
# class UserForm(forms.ModelForm):
#     class Meta:
#         model=User
class UserForm(UserCreationForm):
    email=forms.EmailField(required=True)
    mobile=forms.IntegerField()
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2','mobile']

 
        
        
class LoginForm(forms.Form):
    uname=forms.CharField(max_length=30,label="Username")
    pswd=forms.CharField(max_length=30,label="Password")


