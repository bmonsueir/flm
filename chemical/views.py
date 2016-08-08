from django.shortcuts import render, get_object_or_404
from .models import Chemical
from .models import Project
from .models import Formula

def index(request):
    return render(request, 'chemical/index.html')


def chemical_index(request):
    all_chemical = Chemical.objects.all()
    context = {
        'all_chemical': all_chemical
    }
    return render(request, 'chemical/chemical_index.html', context)
    
def chemical_detail(request, chemical_id):
    chemical = get_object_or_404(Chemical, id = chemical_id)
    return render(request, 'chemical/chemical_detail.html', {'chemical': chemical})
    
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
    
