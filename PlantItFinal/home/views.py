from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request) :
    return render(request, 'index.html')
def home(request) :
    return render(request, 'index.html')
def about(request) :
    return render(request, 'about.html')
def contact(request) :
    return render(request, 'contact.html')
def social(request) :
    return render(request, 'social.html')
def plantfinder(request) :
    return render(request, 'plantfinder.html')