from django import forms
from app_products.models import ProductCategory, Product, ProductImage

class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['category_name', 'short_name', 'is_active']

        widgets = {
            'category_name': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'short_name': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input mb-2'})
        }
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'slug', 'description', 'price', 'category', 'quantity', 'is_active', 'return_policy', 'is_cod_available', 'has_discount', 'has_offer', 'has_vat_included']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'slug': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-2'}),
            'price': forms.NumberInput(attrs={'class': 'form-control mb-2'}),
            'category': forms.Select(attrs={'class': 'form-control mb-2'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control mb-2'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input mb-2'}),
            'return_policy': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'is_cod_available': forms.CheckboxInput(attrs={'class': 'form-check-input mb-2'}),
            'has_discount': forms.CheckboxInput(attrs={'class': 'form-check-input mb-2'}),
            'has_offer': forms.CheckboxInput(attrs={'class': 'form-check-input mb-2'}),
            'has_vat_included': forms.CheckboxInput(attrs={'class': 'form-check-input mb-2'})
        }

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['product', 'image', 'img_order', 'is_featured']