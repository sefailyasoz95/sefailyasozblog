from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from .forms import NewBlog, ReadingCount
from .models import Blog
from pages.models import Setting

def index(request):
    blogs = Blog.objects.filter(status='Yayında').order_by('-created_date')
    settings = Setting.objects.get(pk=1)
    context = {'blogs': blogs, 'settings': settings}
    return render(request, 'blogs/blogs.html', context)

def detail(request, id):
    blogs = Blog.objects.get(pk=id)
    blogs.readings += 1
    blogs.save()
    settings = Setting.objects.get(pk=1)
    context = {'blogs': blogs,'settings': settings}
    return render(request, 'blogs/detail.html', context)

def search(request):
    return render(request, 'blogs/search.html')

def getReadingCount(request, id):
    if request.method == "POST":
        blog = Blog.objects.get(pk=id)
        form = blog(request.POST)
        if form.is_valid():
            blog.readings += 1
            form.save()

@login_required(login_url='/')
def newblog(request):

    if request.method == "POST":
        form = NewBlog(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog kaydedildi")
            return HttpResponseRedirect('/blogs/newblog')

    form = NewBlog()
    context = {'form': form}
    return render(request, 'blogs/newblog.html', context)