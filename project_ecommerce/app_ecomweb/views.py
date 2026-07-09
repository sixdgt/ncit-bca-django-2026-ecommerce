from django.shortcuts import render
from app_products.models import Product, ProductCategory

# Create your views here.
def landing_page(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.filter(is_active=True)
    context = {
        "categories": categories,
        "products": products
    }
    return render(request, 'landing.html', context)

def about_page(request):
    context = {
        "title": "About US",
        "products": ["Product 1", "Product 2", "Product 3"],
    }
    return render(request, 'pages/about.html', context)

def faq_page(request):
    return render(request, 'pages/faq.html')