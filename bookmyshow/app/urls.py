from django.urls import path
from . import views 

urlpatterns=[
        path('index',views.index_page),
        path('view/<id>',views.view_movie),
        
]