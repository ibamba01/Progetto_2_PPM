from django.contrib.auth.models import User

from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

class Product(models.Model):
    user = models.ForeignKey(User, related_name="products", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    description = models.TextField(blank=True)
    price = models.IntegerField() #è il moodo piu comune con cui si rappresentano i prezzi in un database
    image = models.ImageField(upload_to="uploads/product_images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-created_at',) #ordina i prodotti in ordine di creazione


    def __str__(self):
        return self.title

    def get_display_price(self):
        return self.price / 100