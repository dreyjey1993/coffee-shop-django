from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('kontakt/', views.kontakt, name='kontakt'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('gallery/', views.gallery, name='gallery'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.article_detail, name='article_detail'),
    path('reservation/', views.reservation, name='reservation'),
    path('health/', views.health_check, name='health_check'),
    path('sitemap.xml', views.sitemap, name='sitemap'),
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('feed/rss/', views.feed_rss, name='feed_rss'),
]
