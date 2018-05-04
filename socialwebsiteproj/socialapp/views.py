from django.shortcuts import render
from socialapp.forms import *
from django.contrib.auth import authenticate,login
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.contrib import messages
# Create your views here.
def user_login(request):
    if request.method=="POST":
        form=LoginForm(request.POST)#try the form
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(username=cd["username"],password=cd["password"]) #get all the creds, returns a user object
            if user is not None: #if we exsist and are active log us in
                if user.is_active:
                    login(request,user)
                    return HttpResponse("Sucessful Login")
                else:
                    return HttpResponse("User is inactive")
            else:
                messages.error(request,"The user does not exists")
                return HttpResponseRedirect(reverse("login"),"That user does not exist")
    else:
        form=LoginForm()
    return render(request,"login.html",{"form":form})
