from django.shortcuts import render
from project.models import Project
from blog.models import Blog

# Create your views here.
def home(request):
    pjs = Project.objects.order_by('-date')
    blogs = Blog.objects.order_by('-date','-time')
    return render(request,'home/home.html',{'pjs':pjs,'blogs':blogs})