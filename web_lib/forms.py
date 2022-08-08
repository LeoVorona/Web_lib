from cProfile import label
import email
from pyclbr import Class
from django import forms
from .models import Book
from django.forms import widgets
class SearchAuthor(forms.Form):
    author_uuid = forms.UUIDField(label="Author UUID", required=False)

class PostAuthor(forms.Form):
    name = forms.CharField(label="Name", max_length=200, required=False)
    age = forms.IntegerField(label="Age", required=False)
    email = forms.EmailField(label="Email", required=False)

class BookForm(forms.ModelForm): 
    class Meta:
        model = Book
        fields = '__all__'
        labels = {
            'title':'название книги ',
            'description':'описание книги ',
            'page_num':'количество страниц ',
            'author':'выберите автора '
            }
        widgets = {"description":widgets.TextInput}    