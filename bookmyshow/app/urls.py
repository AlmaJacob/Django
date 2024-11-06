from django.urls import path
from . import views 

urlpatterns=[
        path('index',views.index_page),
        path('venom',views.venom_page),
        
]