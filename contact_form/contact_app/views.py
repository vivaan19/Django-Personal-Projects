from django.shortcuts import render, redirect
from .models import contacts
from django.contrib import messages
from datetime import datetime

def base(request):
    return render(request, "base.html")

def submit(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc= request.POST.get('desc')
        contact=contacts(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, "base.html")

# Create your views here.
