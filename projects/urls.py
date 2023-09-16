from django.urls    import include, path
from projects       import views
from projects.views import CreateProjectView

urlpatterns = [
    path('create', CreateProjectView.as_view(), name = "create"),
    path('<int:id>', views.project_page, name = "project_page")
]
