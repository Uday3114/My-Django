from django.shortcuts import render, HttpResponseRedirect
from .forms import signupform
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def signupformmethod(request):
    if request.method == 'POST':
        fm = signupform(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'You Have successfully SIGNED-UP')

    else:
        fm = signupform()
    return render(request,'signupform.html',{'form':fm})

def loginmethod(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                user = fm.cleaned_data['username']
                pwd = fm.cleaned_data['password']
                user = authenticate(username=user,password=pwd)
                if user is not None:
                    login(request,user)
                    messages.success(request,"Logged in Succesfully")
                    return HttpResponseRedirect("/profile/")
        else:
            fm = AuthenticationForm()
            return render(request,'loginform.html',{"form":fm})

    else:
        return HttpResponseRedirect("/profile/")

def userprofile(request):
    if request.user.is_authenticated:
        return render(request,'userprofile.html',{"name":request.user})
    else:
        return HttpResponseRedirect("/login/")

def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/login/')