from django.contrib import admin
from .models import Product, Event, Article, GalleryImage, Reservation, ContactMessage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'order', 'image_thumbnail')
    list_editable = ('order', 'price')
    search_fields = ('name', 'description')
    fields = ('name', 'description', 'price', 'image', 'order')

    def image_thumbnail(self, obj):
        if obj.image:
            return '<img src="{}" width="80" style="object-fit:cover;border-radius:4px;">'.format(obj.image.url)
        return "(kein Bild)"
    image_thumbnail.allow_tags = True
    image_thumbnail.short_description = "Bild"

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'image_thumbnail')
    search_fields = ('title', 'description', 'location')
    list_filter = ('date',)
    fields = ('title', 'description', 'date', 'location', 'image')

    def image_thumbnail(self, obj):
        if obj.image:
            return '<img src="{}" width="80" style="object-fit:cover;border-radius:4px;">'.format(obj.image.url)
        return "(kein Bild)"
    image_thumbnail.allow_tags = True
    image_thumbnail.short_description = "Bild"

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'published_date', 'image_thumbnail')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'content', 'image', 'published_date')

    def image_thumbnail(self, obj):
        if obj.image:
            return '<img src="{}" width="80" style="object-fit:cover;border-radius:4px;">'.format(obj.image.url)
        return "(kein Bild)"
    image_thumbnail.allow_tags = True
    image_thumbnail.short_description = "Bild"

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('caption', 'uploaded_at', 'image_thumbnail')
    search_fields = ('caption',)
    fields = ('caption', 'image')

    def image_thumbnail(self, obj):
        if obj.image:
            return '<img src="{}" width="80" style="object-fit:cover;border-radius:4px;">'.format(obj.image.url)
        return "(kein Bild)"
    image_thumbnail.allow_tags = True
    image_thumbnail.short_description = "Bild"

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date', 'time', 'guests', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('date', 'guests')
    fields = ('name', 'email', 'date', 'time', 'guests')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'created_at')
    search_fields = ('subject', 'name', 'email', 'message')
    list_filter = ('created_at',)
    fields = ('name', 'email', 'subject', 'message', 'created_at')
    readonly_fields = ('created_at',)
