from django import forms
from django.contrib.auth.models import User

from .models import Chemical, Specification, Project, Attribute


class ChemicalForm(forms.ModelForm):

    class Meta:
        model = Chemical
        fields = ['name', 'description']


class SpecificationForm(forms.ModelForm):

    class Meta:
        model = Specification
        fields = ['name', 'min_value', 'max_value', 'test_method']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['name']


class AttributeForm(forms.ModelForm):

    class Meta:
        model = Attribute
        fields = ['name', 'description']
