from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth import authenticate

# Create your views here.
def login(request):
    if request.method == "POST":
        #gets the username and password off the form
        u = request.POST["username"]
        p = request.POST["password"]
        #gives the username and password to the variable user
        user = authenticate(username = u, password = p)
        
        if user is not None:
            auth.login(request, user) # we use auth as we are importing from line 3 and if we don't use auth.login it will conflict like with the logout function underneath
            return redirect("/")
        else:
            return HttpResponse("That user or password is wrong!")
    else:
        return render(request, "accounts/login.html")
    
def register(request):
    return render(request, "accounts/register.html")
    
def logout(request):
    auth.logout(request)
    return redirect('/') 