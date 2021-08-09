from django.shortcuts import render
from .models import Student_Info, Movies


# Create your views here.

def display_student(request):
	student_lst = Student_Info.objects.all()

	return render(request,'studentinfoapp/display.html',{'student':student_lst})

def movies(request):
	movie_lst = Movies.objects.all()

	return render(request,'studentinfoapp/display.html',{'movies':movie_lst})