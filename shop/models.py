from django.db import models

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
