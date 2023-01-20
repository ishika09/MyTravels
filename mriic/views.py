from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ContactForm,NewsLetterForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
# from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    form = NewsLetterForm()
    return render(request, 'mriic/index.html',{'form':form})

def about(request):
    return render(request, 'mriic/about.html')  

def contact(request):
    form=ContactForm()
    if(request.method=='POST'):
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render (request,'mriic/index.html',{'message':'Message Sent Successfully'})
    return render(request,'mriic/contact.html', {'form':form})

def product(request):
    return render(request, 'mriic/product.html')    
    
# def services(request):
#     return render(request, 'mriic/services.html')
    
def newsletter(request):
    if request.method=='POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return render (request,'mriic/index.html',{'message':'Successfully Subscribed to Newsletter'})
        else:
            return render (request,'mriic/index.html',{'message':'Email already exists'})
            
def loginuser(request):
    if request.method=='GET':
        return render(request,'mriic/loginuser.html',{'form':AuthenticationForm()})
    else:
        uname = request.POST['username']
        upwd = request.POST['password']
        user = authenticate(request, username=uname, password=upwd)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request,'mriic/loginuser.html',{'form':AuthenticationForm(),'message':'User Not Found.Try Again.'})
        
def logoutuser(request):
    logout(request)
    return redirect('home')

def signupuser(request):
    if request.method=='GET':
        return render(request,'mriic/signupuser.html',{'form':UserCreationForm()})
    else:
        uname= request.POST['username']
        upwd1= request.POST['password1']
        upwd2= request.POST['password2']
        if upwd1==upwd2:
            try:
                user= User.objects.create_user(username=uname, password=upwd2)
                user.save()
                login(request,user)
            except IntegrityError:
                return render(request,'mriic/signupuser.html',{'form':UserCreationForm(),'message':'Username Already Exist'})
            else:
                return redirect('home')
        else:
            return render(request,'mriic/signupuser.html',{'form':UserCreationForm(),'message':'Password Mismatch Error'})        