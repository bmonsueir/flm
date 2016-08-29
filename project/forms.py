#project
from django import forms
from django.contrib.auth.models import User

from .models import  Project, Group




class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['name']

class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ['name']