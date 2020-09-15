from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse("Hello!")
    return render(request, "hello/index.html")

def greet(request, name):
    # return HttpResponse(f"Hello, {name.capitalize()}! From greet views")
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })

def brian(request):
    return HttpResponse("Hello, Brian!")

def david(request):
    return HttpResponse("Hello, David!")