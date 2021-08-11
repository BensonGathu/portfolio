from django.shortcuts import render
from .models import Project,Languages,Profile
# Create your views here.

def index(request):
    projects = Project.objects.all()
    all_languages = Languages.objects.all()
    context = {
        "projects":projects,
        "all_languages":all_languages
    }
    return render(request,"index.html",context)