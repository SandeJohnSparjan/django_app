from django.shortcuts import render, HttpResponse,redirect
#import userCreation,EditProfile form
from django.contrib.auth.forms import UserCreationForm
#import userChangeForm for editing profile
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
#for profile View
from django.contrib.auth.models import User
#import userCreation form
from accounts.forms import (
    RegistrationForm,
    EditProfileForm
)
#to make sure session is still continuing
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse
#editing views functionality using django
#from django.contrib.auth.decorators import login_required


# Create your views here.

def oldhome(request):
    #creating arguments to be called in templates
    numbers = [1,2,3,4,5]
    args = {'numbers' : numbers}
    return render(request,'accounts/oldhome.html',args)

def register(request):
    #check if form data is posted
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile/')
        else:
            form = RegistrationForm()
            args = {'form': form}
            #check if User is present in DB
            #give a return statement here! Saying Data invalid Enter Valid Details
            return render(request, 'accounts/register.html', args)
    #if user enters data first time
    else:
        form = RegistrationForm()
        args = {'form':form}
        return render(request,'accounts/register.html',args)


def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request,'accounts/profile.html',args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            #go back to the same old url(looks for url defiled with name='view_profile'
            return redirect(reverse('accounts:view_profile'))
        else:
            form = EditProfileForm(instance=request.user)
            args = {'form': form}
            return render(request, 'accounts/edit_profile.html', args)
    else:
        form =EditProfileForm(instance=request.user)
        args = {'form':form}
        return render(request,'accounts/edit_profile.html',args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data= request.POST, user = request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('view_profile'))
        else:
            form = PasswordChangeForm(user = request.user)
            args = {'form': form}
            return render(request, 'accounts/change_password.html',args)
    else:
        form = PasswordChangeForm(user = request.user)
        args ={ 'form':form}
        return render(request, 'accounts/change_password.html',args)