from django.urls import path
from foodApp import views

urlpatterns = [
    path('',views.menu, name='menu/'),
    path('menu/',views.menu,name='menu/')


]