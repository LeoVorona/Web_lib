import imp
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from django.utils.html import format_html
from web_lib.models import Author, Book, Product, Store, ExtUser

# Register your models here.
@admin.register(Author)
class AuthorAdmim(admin.ModelAdmin):
    list_display = ['name', 'age', 'email', 'info']
    change_list_template = 'web_lib/button.html'
    change_form_template = 'web_lib/custom_form.html'
    

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [path('button', self.button)]
        return urls + my_urls


    def button(self,req):
        return redirect('..')

    def info(self, obj):
        return format_html('<br>'.join(obj.info()))
    info.short_description = 'Сводка'

    def change_view(self, request, object_id, form_url="", extra_context = None):
        extra_context = extra_context or {}
        all_books = Author.objects.get(pk=object_id).book_set.all()
        extra_context['books'] = all_books
        return super().change_view(request, object_id, form_url, extra_context)

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