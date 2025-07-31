from django.shortcuts import render
from .models import userlog
from .models import user
from .models import userbill
# Create your views here.
def index(request):
    return render(request,'index.html')
def display(request):
    image=userlog.objects.all()
    price=userlog.objects.all()
    return render(request,'display.html',{"img":image,"price":price})
def login(request):
    msg=" "
    if request.method=="POST":
        b2=request.POST.get("usrname")
        b3=request.POST.get("usrpwd")
        if user.objects.filter(usrname=b2,usrpwd=b3).exists():
            image=userlog.objects.all()
            return render(request,'display.html',{"img":image})
        else:
            msg="user not found"
            return render(request,'userdash.html',{"msg":msg})
    return render(request,'login.html')
def register(request):
    if request.method=="POST":
        b2=request.POST.get("usrname")
        b3=request.POST.get("usrpwd")
        user.objects.create(usrname=b2,usrpwd=b3)
    return render(request,'register.html')
def billing(request):
    if request.method=="POST":
        b4=request.POST.get("prdname")
        b5=request.POST.get("qty")
        b8=request.POST.get("date")
        b9=request.POST.get("time")
        b10=request.POST.get("place")
        b11=request.POST.get("email")
        b12=request.POST.get("adress")
        b13=request.POST.get("phn")
        userbill.objects.create(prdname=b4,qty=b5,date=b8,time=b9,place=b10,email=b11,adress=b12,phn=b13)
    return render(request,'billing.html')
def aboutus(request):
    return render(request,'aboutus.html')
def contact(request):
    return render(request,'contact.html')
def help(request):
    return render(request,'help.html')
def userdash(request):
    return render(request,'userdash.html')