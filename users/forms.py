from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from .models import Profile

from django.core import validators

class UserRegistrationForm(UserCreationForm):
    
    

    class Meta:
        model = User
        fields = ['username','password1', 'password2']

class StaffRegistrationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name',
            'uid',
            'dob',
            'gender',
            'city',
            'state',
            'mail',
        ]

        



class StaffUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['uid', 'name', 'dob', 'gender', 'state', 'city','mail']




class EmailChangeForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email']