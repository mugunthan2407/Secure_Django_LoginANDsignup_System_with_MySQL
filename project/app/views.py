
from django.shortcuts import render,redirect
from app.forms import UserForm
from app.models import User
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render (request,"index.html")

def login(request):
    return render (request,"login.html")

def compare(request):
    if request.method == 'POST':
        un=request.POST["uid"]
        cn=request.POST["cno"]
        data_exists = User.objects.filter(uname=un,ucontact=cn).exists()
        if (data_exists):
            return render(request,"welcome.html")
        else:
            return render(request,"sorry.html")  
        
def newuser(request):
    if request.method == "POST":
        form = UserForm(request.POST) 
        print(form,"form")
        if form.is_valid():
            form.save()
            return render (request,'welcome.html')
    else:
        form = UserForm()
    return render (request,'newuser.html',{'form':form})