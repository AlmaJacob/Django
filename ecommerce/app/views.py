from django.shortcuts import render

# Create your views here.
def login_page(req):
          if 'shop' in req.session:
                  return render(req,'login.html')
          else:
               if req.method=='POST':
                    uname=req.POST['uname']
                    password=req.POST['password']
                    data=authenticate(username=uname,password=password)
                    if data:
                           login(req,data)
                           req

      
