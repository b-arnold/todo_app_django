from django import forms
from django.contrib.auth import forms
from .models import User


class UserCreationForm(forms.UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email')


class UserChangeForm(forms.UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email')
