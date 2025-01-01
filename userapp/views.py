from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.core import mail
from myproject.settings import EMAIL_HOST_USER


# Create your views here.

import logging
logger = logging.getLogger("django")
import sys, os

def login_user(request):
    try:
        raise Exception("Error")

    except Exception as e:
        logger.error("Exception occurred", exc_info=True)

        # Optional: Manually logging some details
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        logger.error(f"Error details: {exc_type}, File: {fname}, Line: {exc_tb.tb_lineno}")
        

        
    logger.info('I print this on the console and the info.log upper')

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

            #sending email
            subject = "Greeting"
            message = f"Hello, {user.first_name} you're signup successfully!"
            recipient_list = [user.email]
            send_mail(subject, message, EMAIL_HOST_USER, recipient_list, fail_silently=True)

            messages.success(request, "Congrats! You're successfully signedUp.")

            return redirect("login-user")
    
    else:
        return HttpResponse("404 - found")
    
