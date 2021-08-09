from django.shortcuts import render

from .forms import StudentRegistration
from .models import Student


def showformdata(request):
    if request.method=="POST":
        fm= StudentRegistration(request.POST)
        if fm.is_valid():
            print('Name:', fm.cleaned_data['name'])
            print('email:', fm.cleaned_data['email'])

    else:
        fm = StudentRegistration()
    return render(request,'formapp/StudentRegistration.html', {'form':fm})

def mydb(request):
    st=Student.objects.all()
    return render(request,'formapp/StudentRegistration.html',{'stu':st})