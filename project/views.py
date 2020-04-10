from django.shortcuts import render
from .models import Project

# Create your views here.
def all_projects(request):
    projects = Project.objects.all()
    return render(request,'project/all_projects.html',{'projects':projects})