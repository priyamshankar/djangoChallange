from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name="index"),
    path('dyn',views.dyn, name="dyn"),
    path ('login',views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register',views.register, name= 'registre'),
]