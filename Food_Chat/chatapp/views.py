from django.shortcuts import render

# Create your views here.

def facebook(request):
	msg = "WELCOME TO FACEBOOK"
	my_dict = {'msg':msg}

	return render(request,'chatapp/fb.html',context=my_dict)

def whatsapp(request):
	msg = "WELCOME TO WHATSAPP"
	my_dict = {'msg':msg}

	return render(request,'chatapp/wtsup.html',context=my_dict)

def instagram(request):
	msg = "WELCOME TO INSTAGRAM"
	my_dict = {'msg':msg}

	return render(request,'chatapp/insta.html',context=my_dict)