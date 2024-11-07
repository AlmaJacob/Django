from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from.models import *
# Create your views here.

def index_page(req):
    data=Movie.objects.all()[:4]
    data1=Movie.objects.all()[4:9]

    return render(req,'index.html',{'data':data,'data1':data})

# def venom_page(req):
#     return render(req,'venom.html')

def view_movie(req,id):
    data=Movie.objects.get(pk=id)
    return render (req,'venom.html',{'data':data})


