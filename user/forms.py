

''' USER FORMS '''

from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from django import forms


#from django.contrib.auth.models import User
from django.db import models
from .models import *

#some logic



class UserRegistrationForm(UserCreationForm):

  username = forms.CharField(widget=forms.TextInput(attrs={'id':'username','class':'box-input'}))
  first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'first','class':'box-input'}))
  last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'second','class':'box-input'}))
  email = forms.EmailField(widget=forms.TextInput(attrs={'id':'email','class':'box-input'}))
  #college = forms.TypedChoiceField(choices=CHOICES)
  dob = forms.DateTimeField(widget=forms.TextInput(attrs={'id':'date','class':'box-input','type':'date'}))
  password1 = forms.CharField(widget=forms.TextInput(attrs={'id':'password1','class':'box-input'}))
  password2 = forms.CharField(widget=forms.TextInput(attrs={'id':'password2','class':'box-input'}))
  

  class Meta:
    model = User
   
    fields= (
      'username',
      'first_name',
      'last_name',
      'email',
      'user_mode',
      'college',
      'dob',
      'password1',
      'password2',
     
       )

class ProfileUpdateForm(forms.ModelForm):
  description = forms.CharField(widget=forms.TextInput())
  

  class Meta:
    model = Profile
    fields = ['img','description']


class UserUpdateForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['email']

class PageUpdateForm(forms.ModelForm):
  #members = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple(),queryset=queryset)
  #members.widget.attrs.update({'style':'display:none;'})
  #members = forms.CharField(widget=forms.TextInput(attrs={'style':'display:none;','class':'box-input'}))
  

  class Meta:
    model = Page
    fields = ['name','members']

class LoginForm(forms.ModelForm):
  username_email = forms.CharField(widget=forms.TextInput(attrs={'id':'username','class':'box-input'}))
  
  password = forms.CharField()
    
  #user = forms.CharField(widget=forms.TextInput(attrs={'id':'username','class':'box-input'}))
  #password = forms.CharField(widget=forms.TextInput(attrs={'id':'username','class':'box-input'}))
  
  class Meta:
    model=User
    fields = ['username_email','password']





