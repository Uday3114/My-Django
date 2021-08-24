from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from .forms import SignupForm
from django.shortcuts import render, redirect
from .forms import AdminChat
from .models import ChatReg
from chat.models import UserProfile

# Create your views here.
def signup(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created Succesfully')
            fm.save()
    else:
        fm = SignupForm()
    return render(request, 'adminreg/signup.html', {'form': fm})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in Succesfully !!!')
                    return HttpResponseRedirect('show')
        else:
            fm = AuthenticationForm()
        return render(request, 'adminreg/user_login.html', {'form': fm})
    else:
        return HttpResponseRedirect('show')


# def show(request):
#         return render(request,'adminview.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')



# Create your views here.
def show(request):
    if request.user.is_authenticated:
        users = UserProfile.objects.all()
        return render(request, 'adminreg/adminview.html', {'book':users})
    else:
        return HttpResponseRedirect('/login')

def update(request, pk):
    data1 = UserProfile.objects.get(pk=pk)
    form = AdminChat(request.POST, instance=data1)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/adminpage1/show')
    else:
        pi = UserProfile.objects.get(pk=pk)
        form = AdminChat(instance=pi)
    return render(request, 'adminreg/adminview.html', {'form': form}) 

def destroy(request, pk):  
    ticket = UserProfile.objects.get(pk=pk)  
    ticket.delete()
    return HttpResponseRedirect('/adminpage1/show')