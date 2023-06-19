from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from home.models import Contact

# Create your views here.

def index(request):
    return render(request, 'index.html')
    
def videos(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'videos.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        messages.success(request, "Your message has been sent successfully!!! Admin will get back to you as soon as possible...")
    return render(request, 'contact.html')

def userLogin(request):
    if request.user.is_anonymous:
        if request.method == "POST":
            username = request.POST.get('username') 
            password = request.POST.get('password') 
            user = authenticate(username=username, password=password)
            if user is not None:
                # A backend authenticated the credentials
                login(request, user)
                return render(request, 'videos.html')
            else:
                # No backend authenticated the credentials
                messages.error(request, "Invalid Credential!!")
    else:
        return redirect('/videos') 
    return render(request,'login.html')

def userCreate(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!!")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!!")
        elif password1 == password2:
            password = password1
            user = User.objects.create_user(username, email, password)
            user.save()
            request.user = user
            return redirect('/videos')
        else:
            messages.error(request, "Passwords didn't matched!!")
    return render(request, 'register.html')

def userLogout(request):
    logout(request)
    return redirect('/')