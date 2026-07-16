from django.shortcuts import render
from app_products.models import Product, ProductCategory
from django.core.paginator import Paginator

# Create your views here.
def landing_page(request):
    categories = ProductCategory.objects.all()
    # product with product images from the ProductImage model
    products = Product.objects.prefetch_related('images').filter(is_active=True)
    context = {
        "categories": categories,
        "products": products,
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

def product_detail(request, slug, product_id):
    product = Product.objects.prefetch_related('images').get(id=product_id, slug=slug)
    context = {
        "product": product
    }
    return render(request, 'pages/product_detail.html', context)

def product_search(request):
    query = request.GET.get('search', '')
    products = Product.objects.prefetch_related('images').filter(title__icontains=query, is_active=True)
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "products": page_obj,
        "query": query
    }
    return render(request, 'pages/product_search.html', context)