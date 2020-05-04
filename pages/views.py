from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from blogs.models import Blog

from .forms import ContactFormu
from .models import Setting, ContactFormMessage
from projects.models import Project

def index(request):
    blogs = Blog.objects.filter(status='Yayında')
    projects = Project.objects.filter(status='Yayında').order_by('-created_date')[:3]
    settings = Setting.objects.all()
    context = {'blogs': blogs, 'settings': settings, 'projects':projects}
    return render(request, 'pages/index.html', context)

def aboutme(request):
    settings = Setting.objects.get(pk=1)
    context = {'settings': settings}
    return render(request, 'pages/about.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.surname = form.cleaned_data['surname']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Your message delivered successfully.. Thank you!")
            return HttpResponseRedirect('/contact')
        else:
            messages.error(request, 'While sending your message an error occured..')
            return HttpResponseRedirect('/contact')
    settings = Setting.objects.get(pk=1)
    form = ContactFormu()
    context = {'settings': settings, 'form': form}
    return render(request, 'pages/contact.html', context)

