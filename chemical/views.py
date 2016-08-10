from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q #what is?
from .forms import ChemicalForm, SpecificationForm, UserForm, AttributeForm
from .models import Chemical, Specification, Attribute
from .models import Project
from .models import Formula

def home(request):
    return render(request, 'chemical/home.html')


def chemical_index(request):
    all_chemical = Chemical.objects.all()
    context = {
        'all_chemical': all_chemical
    }
    return render(request, 'chemical/chemical_index.html', context)
    
def chemical_detail(request, chemical_id):
    chemical_name = get_object_or_404(Chemical, id = chemical_id)
    specifications = Specification.objects.filter(chemical = chemical_id)
    attributes = Attribute.objects.filter(chemical = chemical_id)
    return render(request, 'chemical/chemical_detail.html', {'specifications': specifications, 'attributes': attributes, 'chemical_name': chemical_name, 'chemical_id': chemical_id})
    
def project_index(request):
    all_project = Project.objects.all()
    context = {
        'all_project': all_project
    }
    return render(request, 'chemical/project_index.html', context)
    
def project_detail(request, project_id):
    project = get_object_or_404(Project, id = project_id)
    return render(request, 'chemical/project_detail.html', {'project': project})
    
def formula_index(request):
    all_formula = Formula.objects.all()
    context = {
        'all_formula': all_formula
    }
    return render(request, 'chemical/formula_index.html', context)
    
def formula_detail(request, formula_id):
    formula = get_object_or_404(Formula, id = formula_id)
    return render(request, 'chemical/formula_detail.html', {'formula': formula})
    
def tutorials(request):
    return render(request, 'chemical/tutorials.html')
    
def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'chemical/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                chemical = Chemical.objects.filter(user=request.user)
                return render(request, 'chemical/index.html', {'chemical': chemical})
            else:
                return render(request, 'chemical/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'chemical/login.html', {'error_message': 'Invalid login'})
    return render(request, 'chemical/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                chemical = Chemical.objects.filter(user=request.user)
                return render(request, 'chemical/home.html', {'chemical': chemical})
    context = {
        "form": form,
    }
    return render(request, 'music/register.html', context)

def create_chemical(request):
    if not request.user.is_authenticated():
        return render(request, 'chemical/login.html')
    else:
        form = ChemicalForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            chemical = form.save(commit=False)
            chemical.save()
            return render(request, 'chemical/chemical_detail.html', {'specifications': {}, 'attributes': {}, 'chemical_name': chemical.name, 'chemical_id': chemical.id})
        context = {
            "form": form,
        }
        return render(request, 'chemical/create_chemical.html', context)

def create_specification(request, chemical_id):
    if not request.user.is_authenticated():
        return render(request, 'chemical/login.html')
    else:
        form = SpecificationForm(request.POST or None, request.FILES or None)
        chemical_name = get_object_or_404(Chemical, id = chemical_id)
        if form.is_valid():
            specification = form.save(commit=False)
            specification.chemical = chemical_id
            specification.save()
            return render(request, 'chemical/chemical_index.html')
        context = {
            "form": form,
        }
        return render(request, 'chemical/create_specification.html', context)

def create_attribute(request):
    if not request.user.is_authenticated():
        return render(request, 'chemical/login.html')
    else:
        form = AttributeForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            attribute = form.save(commit=False)
            attribute.user = request.user
            attribute.save()
            return render(request, 'chemical/create_attribute.html', {'attribute': attribute})
        context = {
            "form": form,
        }
        return render(request, 'chemical/create_attribute.html', context)

def update_attribute(request):
    return render(request, 'chemical/update_attribute')
    
def update_specification(request):
    return render(request, 'chemical/update_specification')