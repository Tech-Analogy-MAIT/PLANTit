from django.shortcuts import render, HttpResponse
from home.models import Contact,Plant
from django.contrib import messages

# Create your views here.
def index(request) :
    return render(request, 'index.html')
def home(request) :
    return render(request, 'index.html')
def about(request) :
    return render(request, 'about.html')
def contact(request) :
    if request.method == "POST" :
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
        messages.success(request,'Thank You! Your message has been sent.')
    return render(request, 'contact.html')
def social(request) :
    return render(request, 'social.html')
def plantfinder(request) :
    plants = Plant.objects.all()
    params={'plant': plants}
    return render(request, 'plantfinder.html', params)