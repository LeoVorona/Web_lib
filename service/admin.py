from django.contrib import admin

from .models import Product, Bin, Home

#admin.site.register(Product)
admin.site.register(Bin)

@admin.register(Product)
class ProductAdmim(admin.ModelAdmin):
    list_display = ['id', 'cost', 'title', 'is_active']
    fields = ['id', 'title']
    list_filter = ['cost']
    search_fields = ['title']

#admin.site.register(Product, ProductAdmim)

@admin.register(Home)
class HomeAdmim(admin.ModelAdmin):
    list_display = ['size', 'cost', 'adres', 'bal']
