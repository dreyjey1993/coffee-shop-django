from django.shortcuts import render

def home(request):
    return render(request, 'shop/home.html')

def menu(request):
    return render(request, 'shop/menu.html')

def kontakt(request):
    return render(request, 'shop/kontakt.html')
