from django.urls import include, path
from assets      import views

urlpatterns = [
    path('<str:file_name>', views.asset, name = "asset")
]
