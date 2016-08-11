from django import forms
from django.contrib.auth.models import User

from .models import Chemical, Specification, Attribute, Project, Formula, Batch


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

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['name']

class FormulaForm(forms.ModelForm):

    class Meta:
        model = Formula
        fields = ['name']

class BatchForm(forms.ModelForm):

    class Meta:
        model = Batch
        fields = ['chemical', 'phase', 'amount', 'instruction']
