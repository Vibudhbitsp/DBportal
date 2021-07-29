from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import *
def register(request):
    if request.method == 'POST':
        form = StaffRegistrationForm(request.POST)
        form_user = UserRegistrationForm(request.POST)
        if form.is_valid():
            if form_user.is_valid():
              user = form_user.save()
              staff = form.save(commit=False)
              staff.user = user
              staff.save()
              messages.success(request, f'Your account has been created! You are now able to log in')
              return redirect('login')

            

    else :
        form = StaffRegistrationForm
        form_user = UserRegistrationForm() 
        return render(request, 'users/register.html', {'form' : form, 'form_user':form_user})

@login_required
def update_staff(request):

    if request.method == 'POST':
        p_form = StaffUpdateForm(request.POST,
                                    staff = Profile.objects.filter(user = request.user)[0])

        if p_form.is_valid():
            staff = Profile.objects.filter(user = request.user)[0].save()
            p_form.save()

    else:
        p_form = StaffUpdateForm()

        context = {
            'p_form' : p_form
        }
        return render(request, 'users/update_staff.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('home')

    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {
        'form': form
    })

@login_required
def change_email(request):

    user = request.user
    if request.method == 'POST':
        form = EmailChangeForm(request.POST)
        if form.is_valid():
            form.save()

            user.email = form.cleaned_data['email']
            user.save()

            return redirect('change_email')

    else:
        form = EmailChangeForm()

    return render(request, 'users/change_email.html', {
        'form': form
    })