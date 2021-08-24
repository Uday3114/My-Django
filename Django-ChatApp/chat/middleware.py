from django.http import HttpResponse
from django.shortcuts import render

class MyExceptionMiddleware:
  def __init__(self, get_response):
    self.get_response = get_response
  def __call__(self, request):
    response = self.get_response(request)
    return response
  def process_exception(self, request, exception):
    print("Exception Occured")
    msg = exception
    class_name = exception.__class__.__name__
    print(class_name)
    print(msg)
    return HttpResponse(msg)

class UnderConstructionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = render(request, 'chat/error.html')
        return response