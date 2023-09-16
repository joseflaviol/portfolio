from django.shortcuts       import render, redirect
from .models                import Project
from django.core.exceptions import ObjectDoesNotExist
from django.views           import View

def project_page(request, id: int):
    try:
        project = Project.objects.get(id = id)

        return render(request, "project.html", { "project": project })
    except ObjectDoesNotExist:
        return redirect("index")

class CreateProjectView(View):
    
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("index")
        return render(request, "create.html")
    
    def post(self, request):
        if not request.user.is_authenticated:
            return redirect("index")
        title       = request.POST["title"]
        subtitle    = request.POST["subtitle"]
        description = request.POST["description"]
        reference   = request.POST["reference"]
        
        project = Project(title = title, subtitle = subtitle, description = description, reference = reference)
        project.save()

        return redirect("index")