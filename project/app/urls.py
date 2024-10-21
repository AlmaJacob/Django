from django.urls import path
from . import views 
urlpatterns=[
    path('s',views.fun1),
    path('a',views.fun2),
    path('',views.fun3),
    path('fun4/<b>',views.fun4),
    path('fun5/<int:a>/<int:b>/<int:c>',views.fun5),
    path('index',views.index_page),
    path('demo',views.demo),
    path('second',views.second_page),
    path('todo',views.todo),
    

]