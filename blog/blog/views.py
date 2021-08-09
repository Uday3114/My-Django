from django.shortcuts import render
from django.http import HttpResponse

posts = [

		{
			'title':'Electronics',
			'content':'First post content',

		},
		{

			'title':'Sports',
			'content':'Second post content',

		},
		{

		'title': 'Dressing',
		'content': 'Third post content',

		}

]

def home(request):

	context = {
		'posts':posts
	}
	#return HttpResponse('<h1>Blog Home</h1>')

	return render(request,'blog/home.html',context)

def about(request):
	#return HttpResponse('<h1>Blog About</h1>')
	
	return render(request,'blog/about.html',{'title':'About'})

