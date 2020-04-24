from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Posts,Comment



# Create your views here.
def home(request):
    obj = Posts.objects.all()
    if request.method=="GET":
        q = request.GET.get('q')
        res = Posts.objects.filter(title__icontains="to")

    return render(request,'home.html',{'data':obj,"search":res})

def register(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request, user)
            messages.success(request, ('You have registered...'))
            return redirect('home')
    else:
        form = SignUpForm()

    context = {'form':form}

    return render(request,'register.html',context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            '''messages.success(request, ('You have been Logged In!'))'''
            return redirect('home')
        else:
            messages.error(request, ('Error Logging In - Please check your credentials'))
            return redirect('login')
    else:
        return render(request, 'login.html',{})

def details(request,id):
    item = Posts.objects.get(id=id)
    comment =Comment.objects.filter(post=id) 
    return render(request,'details.html',{'data':item,'comment':comment})

def addpost(request):
    return render(request,'addpost.html',{})

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out'))
    return redirect("home")