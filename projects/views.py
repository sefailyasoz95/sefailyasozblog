from django.shortcuts import render

# Create your views here.

def projects(request):
    return render(request, 'projects/projects.html')

def details(request):
    return render(request, 'projects/details.html')