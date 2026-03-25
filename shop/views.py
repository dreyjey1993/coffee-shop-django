from django.shortcuts import render
from .models import Product

def home(request):
    featured = Product.objects.filter(order__lt=10)[:3]
    return render(request, 'shop/home.html', {'featured': featured})

def menu(request):
    products = Product.objects.all()
    return render(request, 'shop/menu.html', {'products': products})

def kontakt(request):
    return render(request, 'shop/kontakt.html')
