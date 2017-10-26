from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class ProfileForm(forms.ModelForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    class Meta:
        model = Profile
        fields = ('bio', 'birth_date', )

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', )