from django import forms
#from django.db import models
#importing User model to replicate it
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

#adding our fields to the already existing UserCreationForm
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    #telling form some information about itself
    class Meta:
        model=User
        fields ={
            'username','first_name','last_name','email','password1','password2'
        }
    #saving into DB
    def save(self, commit=True):
        user = super(RegistrationForm,self).save(commit=False)
        #cleaned_data is to check the input is clean
        user.first_name= self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

#custom edit profile form
class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        #fields, exclude are variables used to include on exclude in the template
        fields = {
            'email',
            'first_name',
            'last_name',
            'password'
        }

