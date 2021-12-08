from django.shortcuts import render ,HttpResponse
from App import Contact
from datetime import datetime
from django.contrib import messages

def index(request):  # this returns to home page. 
    # return HttpResponse("Hello World Changed the home page of django !!!")
    return render(request, "index.html")

def about(request):
    # return HttpResponse("This is about page !!!")
    return render(request, "about.html")

def contact(request):
    # return HttpResponse("This is a contact page !!!")
    if request.method == "POST":
        name= request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc= request.POST.get('desc')
        contact=Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, "contact.html")

def services(request):
    # return HttpResponse("This is services page !")
    return render(request, "services.html")

# def connect(request):
#     return HttpResponse("This is connect with us page !")
    # return render(request, "myboot_website.html")
# Create your views here.
