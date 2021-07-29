from django import forms

from .models import *
from users.models import *



class FileUploadForm(forms.ModelForm):
    
    class Meta:
        model = Portal
        fields = ['file_name', 'doc']

class SearchUIDForm(forms.Form):
   
    uid = forms.IntegerField()
    

class MailContentForm(forms.Form):
    subject = forms.CharField(max_length = 20)
    content = forms.CharField(max_length = 250)

    

class AddDberForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['uid','user', 'name', 'dob', 'gender', 'city', 'state','mail','qualifier']

