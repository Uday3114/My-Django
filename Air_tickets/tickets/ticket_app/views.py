from django.shortcuts import render, redirect
from .forms import Air_Ticket
from .models import AirTicketModel
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SignupForm
from datetime import datetime, timedelta
# Create your views here.
def show(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = Air_Ticket(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                From = form.cleaned_data['From']
                To = form.cleaned_data['To']
                email = form.cleaned_data['email']
                ticket_no = form.cleaned_data['ticket_no']
                no_of_tickets = form.cleaned_data['no_of_tickets']
                gender = form.cleaned_data['gender']
                age = form.cleaned_data['age']
                reg_data = AirTicketModel(name=name,From=From,To=To,email=email,ticket_no=ticket_no,no_of_tickets=no_of_tickets,gender=gender,age=age)
                reg_data.save()
                form = Air_Ticket()
        else:
            form = Air_Ticket()
        booking = AirTicketModel.objects.all()

        return render(request, 'show.html', {'form': form, 'book':booking})
    else:
        return HttpResponseRedirect('/login')

def update_ticket(request, id):
    ticket = AirTicketModel.objects.get(pk=id)
    form = Air_Ticket(request.POST, instance = ticket)
    if form.is_valid():
        form.save()
        return redirect("/show")
    else:
        pi = AirTicketModel.objects.get(pk=id)
        form = Air_Ticket(instance=pi)
    return render(request, 'show.html', {'form': form})

def destroy(request, id):
    ticket = AirTicketModel.objects.get(id=id)
    ticket.delete()
    return redirect("/show")


# Create your views here.

def signup(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created Succesfully')
            fm.save()
    else:
        fm = SignupForm()
    return render(request, 'user_signup.html', {'form': fm})


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
                    return HttpResponseRedirect('/show')
        else:
            fm = AuthenticationForm()
        return render(request, 'user_login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/show')


# def user_profile(request):
#     if request.user.is_authenticated:
#         return render(request,'show.html',{'name':request.user})
#     else:
#         return HttpResponseRedirect('/login')

def home(request):
    return render(request,'home.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')

def setcookie(request):

 response = render(request, 'setcookie.html')
 #response.set_cookie('name','sonam')
 #response.set_cookie('name','sonam',max_age=120)
 response.set_cookie('lname', 'Jha', expires=datetime.utcnow()+timedelta(days=2))
 return response

def getcookie(request):
  name = request.COOKIES['name']
 # name = request.COOKIES.get('name')
# name = request.COOKIES.get('name', "Guest")
  return render(request, 'getcookie.html', {'name':name})

def delcookie(request):
 reponse = render(request, 'delcookie.html')
 reponse.delete_cookie('name')
 return reponse

def getsession(request):
    name = request.session['name']
    movie_name = request.session['city_name']
    # name = request.session.get('name', default = 'Guest')
    # keys = request.session.keys()
    # key = request.session.items()
    # age = request.session.setdefault('age', '36')
    request.session.modified = True
    context = {'name': name, 'city_name': city_name}
    return render(request, 'getsession.html',context )

def delsession(request):
    # if 'name' in request.session:
    #     del request.session['name']
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'delsession.html')