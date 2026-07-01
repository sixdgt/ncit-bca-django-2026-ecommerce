from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing_page(request):
    context = {
        "title": "DJango Workshop",
        "subtitle": "NCIT | BCA",
        "message": "Welcome to the Django Workshop. This is a sample landing page for the e-commerce project.",
        "year": 2026
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