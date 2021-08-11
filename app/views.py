from django.shortcuts import render
from .models import Project,Languages,Profile
# Create your views here.

def index(request):
    projects = Project.objects.all()
    all_languages = Languages.objects.all()
    current_user = request.user.profile
    context = {
        "projects":projects,
        "all_languages":all_languages,
        "current_user":current_user,
    }
    return render(request,"index.html",context)