from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages


# Create your views here.


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)

            messages.success(request,"Congrats! You're Successfully Loggedin.")
            return redirect("retrieve-view")
        
        else:
            messages.warning(request, "You're login attempt is failed. Please enter a valid credentials!")
            return redirect("home")
        
    else:
        return render(request, "home.html")    
            
        


def signup(request):

    if request.method == "POST":

        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if not password1 == password2:
            messages.warning(request, "Your password is not match!")
        else:    
            user = User.objects.create_user(username, email, password1)

            user.first_name = fname
            user.last_name = lname
            user.save()


            messages.success(request, "Congrats! You're successfully signup.")

            return redirect("login-user")
    
    else:
        return HttpResponse("404 - found")
    


