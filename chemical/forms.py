#chemical
from django import forms
from django.contrib.auth.models import User

from .models import Chemical, Specification, Attribute


class ChemicalForm(forms.ModelForm):

    class Meta:
        model = Chemical
        fields = ['name', 'description']


class SpecificationForm(forms.ModelForm):

    class Meta:
        model = Specification
        fields = ['name', 'min_value', 'max_value', 'test_method']



class AttributeForm(forms.ModelForm):

    class Meta:
        model = Attribute
        fields = ['name', 'description']
