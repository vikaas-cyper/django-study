from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
    dist = {
        "name" : "Vikaas"
    }
    return render(request, 'hello.html', dist)