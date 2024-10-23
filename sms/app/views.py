from django.shortcuts import render
from django.http import HttpResponse
from . models import *

# Create your views here.
def fun1(request):
    return HttpResponse('heyy')
def disp_std(req):
    data=student.objects.all()
    return render(req,'display_std.html',{'data':data})
def add_std(req):
    return render(req,'add_std.html')