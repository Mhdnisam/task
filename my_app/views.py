from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to the homepage!")


def food(request):
    return render(request, 'home.html')


def example(request):
    item = ["apple", "banana", "cherry"]
    return render(request, 'example.html', {"items": item})


def message(request):
    fruits = ["apple", "banana", "mango"]
    return render(request, 'about.html', {"fruits": fruits})
    return HttpResponse("Hello, Django Learner!")
# # Create your views here.
