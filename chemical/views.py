#chemical
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q #what is?
from .forms import ChemicalForm, SpecificationForm, AttributeForm
from .models import Chemical, Specification, Attribute
import simplejson as json
from django.http import HttpResponse
from django.template.context import RequestContext

def home(request):
    return render(request, 'chemical/home.html')

def chemical(request, chemical_id):
    if not request.user.is_authenticated():
        return render(request, 'chemical/login.html')
    else:
        chemical_name = get_object_or_404(Chemical, id = chemical_id)
        chemical = Chemical.objects.filter(id = chemical_id)
        specifications = Specification.objects.filter(chemical = chemical_id)
        form = SpecificationForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            specification = form.save(commit=False)
            specification.chemical = chemical_name
            specification.save()
        form = SpecificationForm() 
        context = {
            "form": form,
            'specifications': specifications,
            "chemical": chemical,
            'chemical_name': chemical_name
        }
    return render(request, 'chemical/chemical.html', context)



        
def chemicals(request):
    if not request.user.is_authenticated():
        return render(request, 'chemical/login.html')
    else:
        all_chemical = Chemical.objects.all()
        context = {
            'all_chemical': all_chemical
        }
        form = ChemicalForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            chemical = form.save(commit=False)
            chemical.save()
        form = ChemicalForm() 
        context = {
            "form": form,
            'all_chemical': all_chemical,
        }
        
        return render(request, 'chemical/chemicals.html', context)
        
