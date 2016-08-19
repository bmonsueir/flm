from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q #what is?
from .forms import ChemicalForm, SpecificationForm, UserForm, ProjectForm, FormulaForm, BatchForm
from .models import Chemical, Specification
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

def projects(request):
    if not request.user.is_authenticated():
        return render(request, 'chemical/login.html')
    else:
        all_project = Project.objects.all()
       
        form = ProjectForm(request.POST or None, request.FILES or None)
       
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
        form = ProjectForm()
        context = {
            "form": form,
            'all_project': all_project
        }
        return render(request, 'chemical/projects.html', context)
        
def formulas(request, project_id):
    if not request.user.is_authenticated():
        return render(request, 'chemical/login.html')
    else:
        form = FormulaForm(request.POST or None, request.FILES or None)
        project_name = get_object_or_404(Project, id = project_id)
        all_formula = Formula.objects.filter(project = project_id)
        if form.is_valid():
            formula = form.save(commit=False)
            formula.project = project_name
            formula.save()
        form = FormulaForm()
        context = {
            "form": form,
            'all_formula': all_formula
        }
        return render(request, 'chemical/formulas.html', context)
        
def batch(request, formula_id):
    if not request.user.is_authenticated():
        return render(request, 'chemical/login.html')
    else:
        form = BatchForm(request.POST or None, request.FILES or None)
        formula_name = get_object_or_404(Formula, id = formula_id)
        batches = Batch.objects.filter(formula = formula_id)
        next_row = 0
        total = 0
        for the_batch in batches:
            total += the_batch.amount
            next_row = the_batch.row
        next_row += 1
        if form.is_valid():
            batch = form.save(commit=False)
            batch.row = next_row
            batch.formula = formula_name
            batch.save()
        form = BatchForm()
        batches = Batch.objects.filter(formula = formula_id)
        context = {
            "form": form,
            'batches': batches,
            "formula_name": formula_name, 
            'total': total
        }
        
        return render(request, 'chemical/batch.html', context)
        
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
        
def read_batch(request, formula_id):
    if not request.user.is_authenticated():
        return render(request, 'chemical/login.html')
    else:
        formula_name = get_object_or_404(Formula, id = formula_id)
        batches = Batch.objects.filter(formula = formula_id)
        total = 0
        for the_batch in batches:
            total += the_batch.amount
        context = {
            'batches': batches,
            "formula_name": formula_name, 
            'formula_id': formula_id,
            'total': total
        }
        
        return render(request, 'chemical/read_batch.html', context)
        
def add_batch(request, formula_id):
    if not request.user.is_authenticated():
        return render(request, 'chemical/login.html')
    else:
        form = BatchForm(request.POST or None, request.FILES or None)
        formula_name = get_object_or_404(Formula, id = formula_id)
        batches = Batch.objects.filter(formula = formula_id)
        next_row = 0
        total = 0
        for the_batch in batches:
            total += the_batch.amount
            next_row = the_batch.row
        next_row += 1
        if form.is_valid():
            batch = form.save(commit=False)
            batch.row = next_row
            batch.formula = formula_name
            batch.save()
        form = BatchForm()
        batches = Batch.objects.filter(formula = formula_id)
        context = {
            "form": form,
            'batches': batches,
            "formula_name": formula_name, 
            'total': total
        }
        
        
        return render(request, 'chemical/add_batch.html', context)
        
        
def save_batch(request, formula_id):
    if not request.user.is_authenticated():
        return render(request, 'chemical/login.html')
    else:
        form = BatchForm(request.POST or None, request.FILES or None)
        formula_name = get_object_or_404(Formula, id = formula_id)
        batches = Batch.objects.filter(formula = formula_id)
        next_row = 0
        total = 0
        for the_batch in batches:
            total += the_batch.amount
            next_row = the_batch.row
        next_row += 1
        if form.is_valid():
            batch = form.save(commit=False)
            batch.row = next_row
            batch.formula = formula_name
            batch.save()
        form = BatchForm()
        batches = Batch.objects.filter(formula = formula_id)
        context = {
            "form": form,
            'batches': batches,
            'formula_name': formula_name, 
            'formula_id': formula_id,
            'total': total
        }
        
        return render(request, 'chemical/add_batch.html', context)