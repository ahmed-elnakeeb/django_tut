from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import tutorial
from  django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from  django.contrib.auth import  login,logout,authenticate
from django.contrib import messages

# Create your views here.
def homepage(request):
    return render(request=request,template_name="main/home.html",
        context={"tutorials":tutorial.objects.all})
        
def profile(request):
    return render(request=request,template_name="main/profile.html")

def signin(request):
    return render(request=request,template_name="main/signin.html")

def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request,"congrates")
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request,f"{msg}:{form.error_messages[msg]}")

    form = UserCreationForm
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            

            messages.success(request,"loged in ")
            username = form.cleaned_data.get('username')
            user =authenticate(username= username,password= password)
            if user is not None:
                login(request, user)
            else:

                return redirect("main:login")

            return redirect("main:homepage")

    form = AuthenticationForm()
    return render(request = request,
                  template_name = "main/login.html",
                  context={"form":form})


def logout_request(request):
    logout(request)

    return redirect("main:homepage")
    