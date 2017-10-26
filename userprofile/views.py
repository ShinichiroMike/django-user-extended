
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from django.forms.models import inlineformset_factory
from .forms import ProfileForm, EditUserForm

@login_required
def profile(request):
    return render(request, 'userprofile/userprofile.html')

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            user_form = UserCreationForm(request.POST)
            profile_form = ProfileForm(request.POST)
            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                user.refresh_from_db()  # This will load the Profile created by the Signal
                profile_form = ProfileForm(request.POST, instance=user.profile)  # Reload the profile form with the profile instance
                profile_form.full_clean()  # Manually clean the form this time. It is implicitly called by "is_valid()" method
                profile_form.save()  # Gracefully save the form
                user = authenticate(username=request.POST['username'], password=request.POST['password1'])
                if user is not None:
                    login(request, user)
                    return redirect('user:profile')
        else:
            user_form = UserCreationForm()
            profile_form = ProfileForm()
        return render(request, 'userprofile/user_profile_form.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })
    else:
        return redirect('user:profile')

def user_edit(request):
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            return redirect('user:profile')
    else:
        user_form = EditUserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'userprofile/user_profile_form.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


