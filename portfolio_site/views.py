from django.shortcuts import render
from .models import Projects
# Create your views here.

def home(request):
    projects = Projects.objects.all()
    return render(request, 'portfolio/index.html', {'projects':projects})