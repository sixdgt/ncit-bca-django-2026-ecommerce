from django.shortcuts import render, redirect, get_object_or_404
from app_products.forms import ProductCategoryForm, ProductForm, ProductImageForm
from app_products.models import ProductCategory, Product, ProductImage
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.
def product_category_create(request):
    if request.method == "POST":
        request_data = request.POST
        form_data = ProductCategoryForm(request_data)
        
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Category created successfully!")
            return redirect("category.create")
        else:
            messages.error(request, "Error creating category. Please check the form for errors.")
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
            messages.success(request, "Product created successfully!")
            return redirect("product.create")
        else:
            messages.error(request, "Error creating product. Please check the form for errors.")
            return redirect("product.create")
    else:
        product_form = ProductForm()
        context = {
            "product_form": product_form,
            "title": "Create Product",
            "button_text": "Create Product"
        }
        return render(request, "products/product_form.html", context)

def product_index(request, *args, **kwargs):
    """
    This view is responsible for displaying all the products in the database.
    """
    # for searching products by name and descriptions
    search_query = request.GET.get('search', '')
    
    products = Product.objects.all() # it returns all the products
    if search_query:
        products = products.filter(title__icontains=search_query) | products.filter(description__icontains=search_query)
    paginator = Paginator(products, 5)  # Show 5 products per page

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    context = {
        "products": products
    }
    return render(request, "products/product_index.html", context)

def product_view(request, pk):
    """
    This view is responsible for displaying a single product based on its primary key (pk).
    """
    product = Product.objects.get(pk=pk) # similar to SELECT * FROM products WHERE id = pk in SQL
    product_images = ProductImage.objects.filter(product=product).order_by('img_order')
    context = {
        "product": product,
        "product_images": product_images
    }
    return render(request, "products/product_detail.html", context)

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
            messages.success(request, "Product updated successfully!")
            return redirect("product.index")
        else:
            messages.error(request, "Error updating product. Please check the form for errors.")
            return redirect("product.edit", pk=pk)
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
    messages.success(request, "Product deleted successfully!")
    return redirect("product.index")

def product_image_add(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        images = request.FILES.getlist('image')
        orders = request.POST.getlist('img_order')

        for i, image in enumerate(images):
            ProductImage.objects.create(
                product=product,
                image=image,
                img_order=int(orders[i]) if i < len(orders) and orders[i] else 0,
                is_featured=(i == 0)
            )

        messages.success(request, "Images added successfully!")
        return redirect("product.view", pk=product_id)
    else:
        form = ProductImageForm()

    return render(request, "products/product_image_form.html", {
        "product_image_form": form,
        "product": product,
        "title": "Add Product Images",
        "button_text": "Upload Images"
    })