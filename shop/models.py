from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    description = models.TextField(verbose_name="Beschreibung", blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Preis (€)")
    image = models.ImageField(upload_to='products/', verbose_name="Bild", blank=True, null=True)
    order = models.IntegerField(default=0, verbose_name="Reihenfolge")

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titel")
    description = models.TextField(verbose_name="Beschreibung", blank=True)
    date = models.DateTimeField(verbose_name="Datum und Uhrzeit")
    location = models.CharField(max_length=200, verbose_name="Ort")
    image = models.ImageField(upload_to='events/', verbose_name="Bild", blank=True, null=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.title} ({self.date.strftime('%d.%m.%Y %H:%M')})"

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titel")
    slug = models.SlugField(unique=True, verbose_name="URL-Slug")
    content = models.TextField(verbose_name="Inhalt")
    published_date = models.DateTimeField(default=timezone.now, verbose_name="Veröffentlichungsdatum")
    image = models.ImageField(upload_to='articles/', verbose_name="Bild", blank=True, null=True)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    caption = models.CharField(max_length=200, verbose_name="Bildunterschrift", blank=True)
    image = models.ImageField(upload_to='gallery/', verbose_name="Bild")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Hochgeladen am")

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.caption or f"Bild {self.id}"

class Reservation(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    email = models.EmailField(verbose_name="E-Mail")
    date = models.DateField(verbose_name="Datum")
    time = models.TimeField(verbose_name="Uhrzeit")
    guests = models.PositiveIntegerField(verbose_name="Personenanzahl")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} – {self.date} {self.time} ({self.guests} Pers.)"
