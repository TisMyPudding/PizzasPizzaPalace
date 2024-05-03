from django.shortcuts import render

# Create your views here.
def order(request):
    order={'output_from_order':'Show each pizza ordered here w/ tax'}
    return render(request, 'orderApp/order.html',context=order)

def tax(request):
    tax={'output_from_tax':'Show each pizza ordered here w tax'}
    return render(request, 'orderApp/tax.html',context=tax)

def cart(request):
    cart={'output_from_cart':'Show each pizza ordered here'}
    return render(request, 'orderApp/cart.html',context=cart)