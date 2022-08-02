from django.urls import path
from web_lib.views import main, authors, author_id, books, book_id, about

urlpatterns = [
    path('', main, name = 'web_lib'),
    path('authors', authors, name = 'authors'),
    path('author/<uuid:pk>', author_id, name = 'author_id'),
    path('books', books, name = 'books'),
    path('book/<int:pk>', book_id, name = 'book_id'),
    path('about', about, name = 'about'),
]