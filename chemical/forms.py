from django import forms
from django.contrib.auth.models import User

from .models import Chemical, Specification, Attribute


class ChemicalForm(forms.ModelForm):

    class Meta:
        model = Chemical
        fields = ['name', 'updatedBy', 'permissions', 'updatedAt']


class SpecificationForm(forms.ModelForm):

    class Meta:
        model = Specification
        fields = ['name', 'max_value', 'min_value', 'test_method', 'updatedBy', 'permissions', 'updatedAt']


class AttributeForm(forms.ModelForm):

    class Meta:
        model = Attribute
        fields = ['name', 'value', 'updatedBy', 'permissions', 'updatedAt']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
