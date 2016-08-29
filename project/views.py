#project
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q #what is?
from .forms import UserForm, ProjectForm, GroupForm
from chemical.models import Chemical, Specification, Attribute
from .models import Project, Group
from formula.models import Formula
import simplejson as json
from django.http import HttpResponse
from django.template.context import RequestContext


    
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
                return render(request, 'chemical/home.html', {'all_project': all_project})
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
     
     
def group(request):
    if not request.user.is_authenticated():
        return render(request, 'chemical/login.html')
    else:
        all_group = Group.objects.all()
       
        form = GroupForm(request.POST or None, request.FILES or None)
       
        if form.is_valid():
            group = form.save(commit=False)
            group.save()
        form = GroupForm()
        context = {
            "form": form,
            'all_group': all_group
        }
        return render(request, 'project/group.html', context)
         
