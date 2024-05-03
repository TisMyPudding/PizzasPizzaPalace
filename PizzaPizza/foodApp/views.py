from django.shortcuts import render
from foodApp.models import Pizzas, Custom

# Create your views here.
def menu(request):
    list=Pizzas.objects.order_by('name')
    menu={'pizza':list}
    return render(request, 'foodApp/menu.html',context=menu)

def custom(request):
    return "pizzas"

def toppings(request):
    return "pizzas"