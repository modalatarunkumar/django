from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def a(request):
    return HttpResponse("Hello world")
def add(request):
    return render(request,"add.html")
def res(request):
    num1=int(request.GET('first'))
    num2=int(request.GET('second'))
    res= num1 + num2
    return render(request,"res.html",{'result':res})