from django.urls          import include, path
from authentication       import views
from authentication.views import Auth

urlpatterns = [
    path('', Auth.as_view(), name = "auth")
]
