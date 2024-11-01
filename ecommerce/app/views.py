from django.shortcuts import render,redirect
from django. http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from . models import *
import os
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def shop_login(req):
          if 'shop' in req.session:
                  return redirect(shop_home)
          if 'user' in req.session:
                  return redirect(user_home)

          
          else:
                if req.method=='POST':
                    username=req.POST['username']
                    password=req.POST['password']
                    data=authenticate(username=username,password=password)
                    if data:
                           login(req,data)
                           if data.is_superuser:
                            req.session['shop']=username  #create
                            return redirect(shop_home)
                           else:
                                   req.session['user']=username  
                                   return redirect(user_home)
                    else:
                       messages.warning(req,'invalid username or password')
                    return render(req,'login.html')
                else:
                       return render(req,'login.html')


def shop_logout(req):
       logout(req)
       req.session.flush()       #delete
       return redirect(shop_login) 

def register(req):
       if req.method=="POST":
              name=req.POST["name"]
              email=req.POST["email"]
              password=req.POST["password"]
              try:
                     data=User.objects.create_user(first_name=name,username=email,email=email,password=password)
                     data.save()
                     return redirect(shop_login)
              except:
                     messages.warning(req,"user details already exists")
       else:
              return render(req,'register.html')

#-----------------admin----------------------------------------------------
def shop_home(req):
       if 'shop' in req.session:
              Products=Product.objects.all()
              return render (req,'shop/shop_home.html',{'Product':Products})
       else:
              return redirect(shop_login)                                                                                                   


def add_product(req):
       if req.method=='POST':
              id=req.POST['pro_id']
              name=req.POST['name']
              price=req.POST['price']
              offer_price=req.POST['offer_price']
              file=req.FILES['img']
              data=Product.objects.create(pro_id=id,name=name,price=price,offer_price=offer_price,img=file)
              data.save()
       return render(req,'shop/add_product.html')

def edit_pro(req,id):
       pro=Product.objects.get(pk=id)
       if req.method=='POST':
              e_id=req.POST['pro_id']
              name=req.POST['name']
              price=req.POST['price']
              offer_price=req.POST['offer_price']
              file=req.FILES.get('img')
              print(file)
              if file:
                     Product.objects.filter(pk=id).update(pro_id=e_id,name=name,price=price,offer_price=offer_price,img=file)
              
              else:
                     Product.objects.filter(pk=id).update(pro_id=e_id,name=name,price=price,offer_price=offer_price)
                     
              return redirect(shop_home)
       return render(req,'shop/edit_product.html',{'data':pro})

def delete_pro(req,id):
       data=Product.objects.get(pk=id)
       url=data.img.url
       url=url.split('/')[-1]
       os.remove('media/'+url)
       data.delete()
       return redirect(shop_home) 



#--------------------user---------------------------
def user_home(req):
       if 'user' in req.session:
              return render(req,'user/user_home.html')

