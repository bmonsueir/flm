from django.shortcuts import render
from django.http import Http404
from .models import Project


def index(request):
    all_project = Project.objects.all()
    context = {
        'all_project': all_project
    }
    return render(request, 'project/index.html', context)
    
def detail(request, project_id):
    try:
        project = Project.objects.get(id = project_id)
    except Project.DoesNotExist:
        raise Http404("Project is not in database")
    return render(request, 'project/detail.html', {'project': project})
    