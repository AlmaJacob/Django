from django.shortcuts import render

# Create your views here.

def index_page(req):
    return render(req,'index.html')

def venom_page(req):
    return render(req,'venom.html')

