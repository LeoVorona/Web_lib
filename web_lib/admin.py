from django.contrib import admin

from web_lib.models import Author, Book

# Register your models here.
@admin.register(Author)
class AuthorAdmim(admin.ModelAdmin):
    list_display = ['name', 'age', 'email']

@admin.register(Book)
class BookAdmim(admin.ModelAdmin):
    list_display = ['title', 'description', 'page_num', 'author']    