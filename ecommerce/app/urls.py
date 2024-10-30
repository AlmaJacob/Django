from django.urls import path
from . import views 

urlpatterns=[
    path('',views.shop_login),
    path('logout',views.shop_logout),

#-----------------------admin----------------------------

path('shop_home',views.shop_home),
path('add',views.add_product),
path('edit/<id>',views.edit_pro),
path('delete/<id>',views.delete_pro),











#-------------------user-------------------------------

]