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

def product_create(request):
    """
    This view is for creating a new product in the database. It handles both GET and POST requests.
    GET: Renders the product creation form.
    POST: Validates and saves the product data to the database.
    """
    if request.method == "POST":
        request_data = request.POST
        form_data = ProductForm(request_data)

        if form_data.is_valid():
            form_data.save()
            return redirect("product.create")
    else:
        product_form = ProductForm()
        context = {
            "product_form": product_form,
            "title": "Create Product",
            "button_text": "Create Product"
        }
        return render(request, "products/product_form.html", context)

def product_index(request):
    """
    This view is responsible for displaying all the products in the database.
    """
    products = Product.objects.all() # similar to SELECT * FROM products in SQL
    context = {
        "products": products
    }
    return render(request, "products/product_index.html", context)

def product_view(request, pk):
    """
    This view is responsible for displaying a single product based on its primary key (pk).
    """
    product = Product.objects.get(pk=pk) # similar to SELECT * FROM products WHERE id = pk in SQL
    context = {
        "product": product
    }
    return render(request, "products/product_view.html", context)

def product_edit(request, pk):
    """
    This view is responsible for editing an existing product based on its primary key (pk).
    GET: Renders the product edit form with existing data.
    POST: Validates and updates the product data in the database.
    """
    product = Product.objects.get(pk=pk)
    if request.method == "POST":
        request_data = request.POST
        form_data = ProductForm(request_data, instance=product)

        if form_data.is_valid():
            form_data.save()
            return redirect("product.index")
    else:
        # re-using product_form.html template for product edit form
        product_form = ProductForm(instance=product)
        context = {
            "product_form": product_form,
            "product": product,
            "title": "Edit Product",
            "button_text": "Update Product"
        }
        return render(request, "products/product_form.html", context)

def product_delete(request, pk):
    """
    This view is responsible for deleting an existing product based on its primary key (pk).
    """
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect("product.index")
