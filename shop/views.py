from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError
from django.utils import timezone
from django.urls import reverse
from .models import Product, Event, Article, GalleryImage, Reservation, ContactMessage

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
    success = False
    if request.method == 'POST':
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )
        success = True
    return render(request, 'shop/kontakt.html', {'success': success})

def about(request):
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

def sitemap(request):
    base_url = request.build_absolute_uri('/')[:-1]
    urls = [
        {'loc': base_url, 'lastmod': timezone.now().date(), 'changefreq': 'daily', 'priority': 1.0},
        {'loc': f'{base_url}{reverse("menu")}', 'lastmod': timezone.now().date(), 'changefreq': 'weekly', 'priority': 0.9},
        {'loc': f'{base_url}{reverse("about")}', 'lastmod': timezone.now().date(), 'changefreq': 'monthly', 'priority': 0.7},
        {'loc': f'{base_url}{reverse("events")}', 'lastmod': timezone.now().date(), 'changefreq': 'weekly', 'priority': 0.8},
        {'loc': f'{base_url}{reverse("gallery")}', 'lastmod': timezone.now().date(), 'changefreq': 'monthly', 'priority': 0.7},
        {'loc': f'{base_url}{reverse("blog")}', 'lastmod': timezone.now().date(), 'changefreq': 'weekly', 'priority': 0.8},
        {'loc': f'{base_url}{reverse("kontakt")}', 'lastmod': timezone.now().date(), 'changefreq': 'monthly', 'priority': 0.6},
        {'loc': f'{base_url}{reverse("reservation")}', 'lastmod': timezone.now().date(), 'changefreq': 'monthly', 'priority': 0.6},
    ]
    for article in Article.objects.filter(published_date__lte=timezone.now()):
        urls.append({
            'loc': f'{base_url}{reverse("article_detail", args=[article.slug])}',
            'lastmod': article.published_date.date(),
            'changefreq': 'monthly',
            'priority': 0.5
        })
    for product in Product.objects.all():
        urls.append({
            'loc': f'{base_url}{reverse("menu")}#product-{product.id}',
            'lastmod': timezone.now().date(),
            'changefreq': 'monthly',
            'priority': 0.3
        })
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls:
        xml += f'''  <url>
    <loc>{u['loc']}</loc>
    <lastmod>{u['lastmod']}</lastmod>
    <changefreq>{u['changefreq']}</changefreq>
    <priority>{u['priority']}</priority>
  </url>\n'''
    xml += '</urlset>'
    return HttpResponse(xml, content_type='application/xml')

def robots_txt(request):
    lines = [
        "User-agent: *",
        "Allow: /",
        "Sitemap: " + request.build_absolute_uri('/sitemap.xml'),
        ""
    ]
    return HttpResponse("\n".join(lines), content_type='text/plain')

def custom_404(request, exception):
    return render(request, 'shop/404.html', status=404)

def custom_500(request):
    return render(request, 'shop/500.html', status=500)