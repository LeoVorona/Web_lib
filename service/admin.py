from django.contrib import admin

from .models import Product, Bin

#admin.site.register(Product)
admin.site.register(Bin)
@admin.register(Product)
class ProductAdmim(admin.ModelAdmin):
    list_display = ['id', 'cost', 'title']
    fields = ['id', 'title']
    list_filter = ['cost']
    search_fields = ['title']

#admin.site.register(Product, ProductAdmim)