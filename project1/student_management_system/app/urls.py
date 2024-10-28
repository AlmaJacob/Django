from django.urls import path
from . import views

urlpatterns=[
      path('sms',views.sms_page),
    path('edit/<id>',views.edit_form),
    path('delete/<id>',views.delete_form),
    
]