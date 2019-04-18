from django.http import HttpResponse
from django.shortcuts import render 

def about(request):
  # return HttpResponse("hello world!!!!!!")
  return render(request, 'about.html')
def home(request):
    # return HttpResponse('this is Home')
  return render(request,'home.html')