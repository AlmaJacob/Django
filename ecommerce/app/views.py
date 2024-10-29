from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from . models import *

# Create your views here.
def shop_login(req):
          if 'shop' in req.session:
                  return redirect(shop_home)
          
          else:
                if req.method=='POST':
                    username=req.POST['username']
                    password=req.POST['password']
                    data=authenticate(username=username,password=password)
                    if data:
                           login(req,data)
                           req.session['shop']=username  #create
                           return redirect(shop_home)
                return render(req,'login.html')


def shop_logout(req):
       logout(req)
       req.session.flush()       #delete
       return redirect(shop_login) 


def shop_home(req):
       if 'shop' in req.session:
              Products=Product.objects.all()
              return render (req,'shop/shop_home.html',{'Product':Products})
       else:
              return redirect(shop_login)      
