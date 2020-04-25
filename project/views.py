from django.shortcuts import render,get_object_or_404
from .models import Project

# Create your views here.
def all_projects(request):
    pjs = Project.objects.order_by('-date')
    return render(request,'project/all_projects.html',{'pjs':pjs})

def detail(request,project_id):
    pj = get_object_or_404(Project,pk=project_id)
    return render(request,'project/detail.html',{'pj':pj})