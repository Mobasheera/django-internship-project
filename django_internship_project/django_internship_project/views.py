from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello, This is our First Django Website")
    return render(request, 'home.html')

def about(request):
    return HttpResponse("Hello, This is our About Page")

def contact(request):
    return HttpResponse("Hello, This is our Contact Page")