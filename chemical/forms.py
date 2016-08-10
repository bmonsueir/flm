from django import forms
from django.contrib.auth.models import User

from .models import Chemical, Specification, Attribute


class ChemicalForm(forms.ModelForm):

    class Meta:
        model = Chemical
        fields = ['name']


class SpecificationForm(forms.ModelForm):

    class Meta:
        model = Specification
        fields = ['name', 'max_value', 'min_value', 'test_method']


class AttributeForm(forms.ModelForm):

    class Meta:
        model = Attribute
        fields = ['name', 'value']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
