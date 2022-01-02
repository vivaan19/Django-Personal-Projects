from django.shortcuts import render ,HttpResponse, redirect
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import blog_model

def base(request):
    obj = blog_model.objects.all()
    username = blog_model.objects.values("name").distinct()
    return render(request, "base.html", {'obj':obj, 'username':username})

def index(request):
    obj = blog_model.objects.all()
    return render(request, "1_index.html", {'obj':obj})

def post(request, var):
    my_post =  blog_model.objects.get(id = var)
    return render(request, "5_posts.html", {'my_post':my_post})

# def user(request, nam):
#     user_obj = blog_model.objects.values("name").distinct()
#     all_obj = blog_model.objects.all()
#     return render(request, "6_user.html", {'all_obj':all_obj, "user_obj": user_obj})

def blog(request):
    if request.method == "POST":
        name = request.POST['name']
        blog_title = request.POST['title']
        body = request.POST['body']

        if name == "" or blog_title == "" or body == "":
            messages.warning(request, "Enter Full details")
            return redirect("blog")
        else:
            amount_of_words = len(body.strip().split())
            if amount_of_words < 100:
                messages.warning(request, f"Blog should be 100 words minimum, your words is {amount_of_words}")
                # return redirect("blog")
            else:
                blog_obj = blog_model(name=name, blog_title=blog_title, content=body)
                blog_obj.save()
                messages.success(request, "Blog Posted!!")
                return redirect(index)
    return render(request, "2_blog.html")

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST.get('email')
        password = request.POST['password']
        repeat_pass = request.POST['password2']

        if password == repeat_pass:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already registered")
                return redirect("register")
            
            elif User.objects.filter(email = email).exists():
                messages.info(request, "Email Already Registerd")
                return redirect("register")

            else:
                user = User.objects.create_user(username=username, email = email, password = password)
                user.save();
                messages.info(request, "User Registered!!!")
                return redirect('login')
        
        else:
            messages.info(request, "Password is not same")
            return redirect("register")
    return render(request, "4_register.html")

def login(request):
    if request.method == "POST":
        # get data input 
        username = request.POST['username']
        password = request.POST['password']

        # Then authenticate user 
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, "Logged In Successfully")
            return redirect("blog")
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')
    return render(request, "3_login.html")

def logout(request):
    auth.logout(request)
    return redirect("index")

# Create your views here.
