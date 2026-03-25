from django.contrib import admin
from .models import Product

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
