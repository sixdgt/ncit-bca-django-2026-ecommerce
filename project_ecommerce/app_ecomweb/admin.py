from django.contrib import admin
from app_ecomweb.models import WebsiteSettings, MetaDescription, CompanyDocument

# Register your models here.
class AdminWebsiteSettings(admin.ModelAdmin):
    list_display = ('site_name', 'contact_email', 'contact_phone', 'company_name', 'address', 'created_at') # to display the site name, contact email, contact phone, company name, and creation date in the list view of website settings
    search_fields = ('site_name', 'contact_email', 'contact_phone') # to search the list of website settings based on site name, contact email, and contact phone
    list_filter = ('is_active',) # to filter the list of website settings based on their active status
    ordering = ('-created_at',) # to order the list of website settings by their creation date in descending order

admin.site.register(WebsiteSettings, AdminWebsiteSettings)
admin.site.register(MetaDescription)
admin.site.register(CompanyDocument)

# changing admin panel site settings
admin.site.site_header = "My E-commerce"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Welcome to E-commerce Admin Panel"
