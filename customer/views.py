from django.shortcuts import render
from django.http import Http404
from .models import Customer


def index(request):
    all_customer = Customer.objects.all()
    context = {
        'all_customer': all_customer
    }
    return render(request, 'customer/index.html', context)
    
def detail(request, customer_id):
    try:
        customer = Customer.objects.get(id = customer_id)
    except Customer.DoesNotExist:
        raise Http404("customer is not in database")
    return render(request, 'customer/detail.html', {'customer': customer})
    