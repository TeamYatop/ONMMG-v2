from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "restaurants/index.html")

def detail(request):
    return render(request, "restaurants/detail.html")

def create(request):
    return render(request, "restaurants/create.html")
