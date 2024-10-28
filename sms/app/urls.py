from django.urls import path
from . import views

urlpatterns=[
    path('',views.fun1),
    path('disp',views.disp_std),
    path('add',views.add_std),
    path('edit/<id>',views.edit_std),
    path('delete/<id>',views.delete_std)

]