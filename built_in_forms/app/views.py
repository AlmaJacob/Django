from django.shortcuts import render,redirect
from .models import *
from .forms import *


# Create your views here.
def normal_form_fun(req):
    if req.method=='POST':
        form1=Normal_form(req.POST)
        if form1.is_valid():
            name=form1.cleaned_data['name']
            age=form1.cleaned_data['age']
            email=form1.cleaned_data['email']
            place=form1.cleaned_data['place']
            data=Project_user.objects.create(name=name,age=age,email=email,place=place)
            data.save()
            return redirect(normal_form_fun)
    form=Normal_form()
    return render(req,'normal_form.html',{'form':form})


def model_form_fun(req):
    form=Model_Form()
    return render(req,'model_form.html',{'form':form})