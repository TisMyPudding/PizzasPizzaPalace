from django.shortcuts import render

# Create your views here.
def signIn(request):
    signIn={'output_from_signIn':'Show if correct username and password'}
    return render(request, 'userApp/signIn.html',context=signIn)

def cardValid(request):
    cardValid={'output_from_cardValid':'Show card being correct length'}
    return render(request, 'userApp/cardValid.html',context=cardValid)

def display(request):
    display={'output_from_display':'Show user info'}
    return render(request, 'userApp/display.html',context=display)