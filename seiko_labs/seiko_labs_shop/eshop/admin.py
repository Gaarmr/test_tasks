from django.contrib import admin
from .models import Category, Product, Shop

# Register your models here.

class ShopAdmin(admin.ModelAdmin):
    list_display = ["id", 'name', 'address', 'rating', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", 'name', 'slug', 'shop']
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", 'name', 'slug', 'price', 'category', 'stock', 'available', 'created', 'updated', 'update_counter']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Shop, ShopAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)