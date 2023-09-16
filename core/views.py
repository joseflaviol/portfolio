from django.shortcuts import render
from projects.models  import Project

def index(request):
    return render(request, "index.html", { "projects": Project.objects.all() })
