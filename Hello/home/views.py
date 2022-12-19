from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request) :
    return render(request, 'index.html')
def home(request) :
    return render(request, 'index.html')
def about(request) :
    return render(request, 'about.html')
def contactus(request) :
    return render(request, 'contactus.html')
def social(request) :
    return render(request, 'social.html')