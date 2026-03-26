from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Product, Event, Article, GalleryImage, Reservation

def home(request):
    featured = Product.objects.filter(order__lt=10)[:3]
    next_events = Event.objects.filter(date__gte=timezone.now())[:3]
    latest_articles = Article.objects.filter(published_date__lte=timezone.now())[:3]
    return render(request, 'shop/home.html', {
        'featured': featured,
        'next_events': next_events,
        'latest_articles': latest_articles,
    })

def menu(request):
    products = Product.objects.all()
    return render(request, 'shop/menu.html', {'products': products})

def kontakt(request):
    return render(request, 'shop/kontakt.html')

def about(request):
    # Philosophie und Team (statisch; später aus DB)
    team = [
        {'name': 'Anna', 'role': 'Barista & Inhaberin', 'image': 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=300&q=80'},
        {'name': 'Ben', 'role': 'Kaffee-Experte', 'image': 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=300&q=80'},
        {'name': 'Clara', 'role': 'Bäckerin', 'image': 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?auto=format&fit=crop&w=300&q=80'},
    ]
    return render(request, 'shop/about.html', {'team': team})

def events(request):
    upcoming = Event.objects.filter(date__gte=timezone.now())
    return render(request, 'shop/events.html', {'events': upcoming})

def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'shop/gallery.html', {'images': images})

def blog(request):
    articles = Article.objects.filter(published_date__lte=timezone.now())
    return render(request, 'shop/blog.html', {'articles': articles})

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'shop/article_detail.html', {'article': article})

def reservation(request):
    success = False
    if request.method == 'POST':
        Reservation.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            date=request.POST.get('date'),
            time=request.POST.get('time'),
            guests=int(request.POST.get('guests', 2))
        )
        success = True
    return render(request, 'shop/reservation.html', {'success': success})
