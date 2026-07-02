from django import forms
from app_products.models import ProductCategory, Product, ProductImage

class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['category_name', 'short_name', 'is_active']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'slug', 'description', 'price', 'category', 'quantity', 'is_active', 'return_policy', 'is_cod_available', 'has_discount', 'has_offer', 'has_vat_included']

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['product', 'image', 'img_order', 'is_featured']