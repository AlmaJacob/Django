from django.shortcuts import render,redirect
from django. http import HttpResponse
sms=[]
# Create your views here.
def sms_page(req):
    if req.method=='POST':
        roll_no=req.POST['roll_no']
        name=req.POST['name']  
        age=req.POST['age'] 
        mark=req.POST['mark'] 
        email=req.POST['email'] 
        phno=req.POST['phno'] 
        sms.append({'roll_no': roll_no,'name': name,'age':age,'mark':mark,'email':email,'phno':phno})
        print(sms)
        return redirect(sms_page)
    return render(req,'sms.html',{'sms':sms})
def edit_form(req,roll_no):
    name=''
    for i in sms:
        if i['roll_no']==roll_no:
            name=i
    if req.method=='POST':
        roll_no=req.POST['roll_no']
        name1=req.POST['name']
        name['roll_no']=roll_no
        name['name']=name1
        return redirect(sms_page)
    return render(req,'edit.html',{'name':name})

def delete_form(req,roll_no):    
        for i in sms:
            if i['roll_no']==roll_no:
                sms.remove(i)
        return redirect(sms_page)     

