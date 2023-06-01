from django.shortcuts import render, get_object_or_404

from .models import Product, Category

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()#prendi tutti i prodotti della categoria

    return render(request, "category_detail.html", {"category": category, "products": products})

def product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug) #matcha la slug del prodoto con la slug del url e fa aprire la pagina, se non la trova da errore 404
    return render(request, "product_detail.html", {"product": product})
