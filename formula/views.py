from django.shortcuts import render
from django.http import Http404
from .models import Formula


def index(request):
    all_formula = Formula.objects.all()
    context = {
        'all_formula': all_formula
    }
    return render(request, 'formula/index.html', context)
    
def detail(request, formula_id):
    try:
        formula = Formula.objects.get(id = formula_id)
    except Formula.DoesNotExist:
        raise Http404("Formula is not in database")
    return render(request, 'formula/detail.html', {'formula': formula})
    