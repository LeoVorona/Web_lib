from genericpath import exists
from django.core.management.base import BaseCommand
from web_lib.models import Book

class Command(BaseCommand):
    help = 'Checking database'

    def add_arguments(self, parser):
        parser.add_argument('book_ids', help='book id', type = int, nargs='+')

    def handle(self, *args, **kwargs):
        book_ids = kwargs['book_ids']
        for book_id in book_ids:
            try:    
                Book.objects.get(pk=book_id)
                self.stdout.write(self.style.SUCCESS('Book with pk = "%s" exist' % book_id))
            except Book.DoesNotExist:
                self.stdout.write(self.style.ERROR('Book with pk = "%s" not found' % book_id))
