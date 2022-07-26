from django.contrib import admin

from web_lib.models import Author, Book, Product, Store, ExtUser

# Register your models here.
@admin.register(Author)
class AuthorAdmim(admin.ModelAdmin):
    list_display = ['name', 'age', 'email']

@admin.register(Book)
class BookAdmim(admin.ModelAdmin):
    list_display = ['title', 'description', 'page_num', 'author']    

@admin.register(ExtUser)
class ExtUserAdmim(admin.ModelAdmin):
    list_display = ['desc', 'is_logged']    

@admin.register(Product)
class ProductAdmim(admin.ModelAdmin):
    list_display = ['name']    

@admin.register(Store)
class StoreAdmim(admin.ModelAdmin):
    list_display = ['name']    