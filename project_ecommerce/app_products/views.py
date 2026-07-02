from django.shortcuts import render, redirect
from app_products.forms import ProductCategoryForm, ProductForm, ProductImageForm
from app_products.models import ProductCategory, Product, ProductImage

# Create your views here.
def product_category_create(request):
    if request.method == "POST":
        request_data = request.POST
        form_data = ProductCategoryForm(request_data)
        
        if form_data.is_valid():
            form_data.save()
            return redirect("category.create")
        
    category_form = ProductCategoryForm()
    context = {
        "category_form": category_form
    }
    return render(request, "categories/category_create.html", context)
