from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *

# Create your views here.
def fun1(request):
    return HttpResponse('heyy')
def disp_std(req):
    data=student.objects.all()
    return render(req,'display_std.html',{'data':data})
def add_std(req):
    if req.method=="POST":
        roll=req.POST["roll_no"]
        std_name=req.POST["name"]
        std_age=req.POST["age"]
        std_email=req.POST["email"]
        std_phno=req.POST["phno"]
        data=student.objects.create(roll_no=roll,name=std_name,age=std_age,email=std_email,phno=std_phno)
        data.save()
        return redirect(disp_std)
    else:
        return render(req,'add_std.html')

def edit_std(req,id):
    data=student.objects.get(pk=id)
    if req.method=="POST":
        roll=req.POST["roll_no"]
        std_name=req.POST["name"]
        std_age=req.POST["age"]
        std_email=req.POST["email"]
        std_phno=req.POST["phno"]
        student.objects.filter(pk=id).update(roll_no=roll,name=std_name,age=std_age,email=std_email,phno=std_phno)
        return redirect(disp_std)
    else:
        return render(req,'edit_std.html',{'data':data})

def delete_std(req,id):
     data=student.objects.get(pk=id)
     data.delete()
     return redirect(disp_std)


