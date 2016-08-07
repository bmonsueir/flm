from django.shortcuts import render
from django.http import Http404
from .models import Chemical


def index(request):
    all_chemical = Chemical.objects.all()
    context = {
        'all_chemical': all_chemical
    }
    return render(request, 'chemical/index.html', context)
    
def detail(request, chemical_id):
    try:
        chemical = Chemical.objects.get(id = chemical_id)
    except Chemical.DoesNotExist:
        raise Http404("Chemical is not in database")
    return render(request, 'chemical/detail.html', {'chemical': chemical})
    