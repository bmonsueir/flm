from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q #what is?
from .forms import ChemicalForm, SpecificationForm, UserForm, AttributeForm, ProjectForm, FormulaForm, BatchForm
from .models import Chemical, Specification, Attribute
from .models import Project
from .models import Formula, Batch

def home(request):
    return render(request, 'chemical/home.html')

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'chemical/home.html')
    else:
        all_project = Project.objects.filter(updatedBy=request.user)
        return render(request, 'chemical/project_index.html', {'all_project': all_project})

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
    formulas = Formula.objects.filter(project = project.id)
    return render(request, 'chemical/project_detail.html', {'project': project, 'project_id': project_id, 'formulas': formulas})
    
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
                all_project = Project.objects.filter(user=request.user)
                return render(request, 'chemical/project_index.html', {'all_project': all_project})
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
    return render(request, 'chemical/register.html', context)

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
        specifications = Specification.objects.filter(chemical = chemical_id)
        attributes = Attribute.objects.filter(chemical = chemical_id)
        if form.is_valid():
            specification = form.save(commit=False)
            specification.chemical = chemical_name
            specification.save()
            return render(request, 'chemical/chemical_detail.html', {'specifications': specifications, 'attributes': attributes, 'chemical_name': chemical_name, 'chemical_id': chemical_id})
        context = {
            "form": form,
            "chemical_name": chemical_name,
        }
        return render(request, 'chemical/create_specification.html', context)

def create_attribute(request, chemical_id):
    if not request.user.is_authenticated():
        return render(request, 'chemical/login.html')
    else:
        form = AttributeForm(request.POST or None, request.FILES or None)
        chemical_name = get_object_or_404(Chemical, id = chemical_id)
        specifications = Specification.objects.filter(chemical = chemical_id)
        attributes = Attribute.objects.filter(chemical = chemical_id)
        if form.is_valid():
            attribute = form.save(commit=False)
            attribute.chemical = chemical_name
            attribute.save()
            return render(request, 'chemical/chemical_detail.html', {'specifications': specifications, 'attributes': attributes, 'chemical_name': chemical_name, 'chemical_id': chemical_id})
        context = {
            "form": form,
            "chemical_name": chemical_name,
        }
        return render(request, 'chemical/create_attribute.html', context)

def create_project(request):
    if not request.user.is_authenticated():
        return render(request, 'chemical/login.html')
    else:
        form = ProjectForm(request.POST or None, request.FILES or None)
        projects = Project.objects.all()
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return render(request, 'chemical/project_index.html', { 'projects': projects})
        context = {
            "form": form,
        }
        return render(request, 'chemical/create_project.html', context)
        
def create_formula(request, project_id):
    if not request.user.is_authenticated():
        return render(request, 'chemical/login.html')
    else:
        form = FormulaForm(request.POST or None, request.FILES or None)
        project_name = get_object_or_404(Project, id = project_id)
        formulas = Formula.objects.all()
        if form.is_valid():
            formula = form.save(commit=False)
            formula.project = project_name
            formula.save()
            return render(request, 'chemical/create_batch.html', {'formula':formula})
        context = {
            "form": form,
        }
        return render(request, 'chemical/create_formula.html', context)
        
def batch(request, formula_id):
    if not request.user.is_authenticated():
        return render(request, 'chemical/login.html')
    else:
        form = BatchForm(request.POST or None, request.FILES or None)
        formula_name = get_object_or_404(Formula, id = formula_id)
        batches = Batch.objects.filter(formula = formula_name)
        print(batches)
        next_row = 0
        for the_batch in batches:
            next_row = the_batch.row
        next_row += 1
        if form.is_valid():
            batch = form.save(commit=False)
            batch.row = next_row
            batch.formula = formula_name
            batch.save()
            batches = Batch.objects.filter(formula = formula_name)
            form = BatchForm(request.POST or None, request.FILES or None)
            return render(request, 'chemical/batch.html', { 'batches': batches, 'formula_name': formula_name, 'form': form})
        context = {
            "form": form,
            'batches': batches,
            "formula_name": formula_name
        }
        return render(request, 'chemical/batch.html', context)