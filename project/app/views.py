from django.shortcuts import render,redirect
from django. http import HttpResponse
todo=[]

# Create your views here.
def fun1(request):
    return HttpResponse ("heyyy")

def fun2(request):
    return HttpResponse ("heloooo")
def fun3(request):
    a={'name':'anu','age':21}
    return HttpResponse(a)
def fun4(request,b):
    return HttpResponse(b)
def fun5(request,a,b,c):
    if a<b and a<c:
        return HttpResponse(a)
    elif b<a and b<c:
        return HttpResponse(b)
    else:
        return HttpResponse(c)
def index_page(req):
    Name='alma'
    age=21
    place='ksrgd'
    return render(req,'index.html',{'Name':Name,'age':age,'place':place})

def demo(req):
    l={'name':'alma','age':21}
    d={'name':'alen','age':28}
    return render(req,'demo.html',{'data1':l},{'data2':d})   
def second_page(req):
    return render(req,'second.html')
def todo(req):
    if req.method=='POST':
        id=req.POST['id']
        task=req.POST['task']  
        todo.append({'id': id,'task': task})
        print(todo)
        return redirect(todo)
    return render(req,'todo.html',{'todo':todo})