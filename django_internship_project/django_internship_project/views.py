from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, This is our First Django Website")

def about(request):
    return HttpResponse("Hello, This is our About Page")

def contact(request):
    return HttpResponse("Hello, This is our Contact Page")