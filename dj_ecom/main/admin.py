from django.contrib import admin
from .models import Product
# Register your models here.


# admin.site.register(Product)

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discount_price', 'category', 'product_image']
