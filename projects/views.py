from django.shortcuts import render

# Create your views here.
from .models import Project
from pages.models import Setting

def projects(request):
    projects = Project.objects.all()
    settings = Setting.objects.all()
    context = {
        'setting': settings,
        'projects': projects,
    }
    return render(request, 'projects/projects.html', context)

def details(request, id):
    project = Project.objects.get(pk=id)
    settings = Setting.objects.get(pk=1)
    context = {
        'settings': settings,
        'project': project
    }
    return render(request, 'projects/details.html', context)