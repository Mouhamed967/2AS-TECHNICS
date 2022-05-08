from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages


def Login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        username = ""
        try:
            username = User.objects.get(email=email.lower()).username
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request,"Welcome back !")
                return redirect("home")
            else:
                messages.error(request, "Incorrect password please try again !")
        except ObjectDoesNotExist:
            messages.error(request, "Invalid email. Please try again a matching email and password !")
    return render(request,'comptes/login.html')

def Logout(request):
    logout(request)
    return  redirect('accueil')



def ResetPassword(request,id): 
    try: 
        user = User.objects.get(pk=id)
        print(user)
        user.set_password("passer2as")
        user.save()
        messages.success(request, "Reset Password {} {} done".format(user.first_name, user.last_name))
    except:
        messages.error(request, "Une erreur s'est produite !")
    
    return redirect('home')
