from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    category_name = models.CharField(max_length=100, null=False, blank=False)
    short_name = models.CharField(max_length=50, null=False, blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=True, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False)
    return_policy = models.CharField(max_length=200, null=True, blank=True)
    is_cod_available = models.BooleanField(default=True)
    has_discount = models.BooleanField(default=False)
    has_offer = models.BooleanField(default=False)
    has_vat_included = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    removed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='product_images/')
    img_order = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.product.title}"
    
    def save(self, *args, **kwargs):
        if self.is_featured:
            ProductImage.objects.filter(product=self.product, is_featured=True).update(is_featured=False)
        super().save(*args, **kwargs)