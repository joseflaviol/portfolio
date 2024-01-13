from django.shortcuts    import render, redirect
from django.views        import View
from django.contrib.auth import authenticate, login

class Auth(View):
    
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, "auth.html")
        return redirect("index")
        
    
    def post(self, request):
        if request.user.is_authenticated:
            return redirect("index")

        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
        else:
            return render(request, "auth.html", { "error": "Username or Password incorrect", "username": username, "password": password })

        return redirect("index")