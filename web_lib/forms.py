from cProfile import label
import email
from pyclbr import Class
from turtle import color
from django import forms
from .models import Book
from django.forms import widgets
from django.core import validators
from django.core.exceptions import ValidationError

class SearchAuthor(forms.Form):
    author_uuid = forms.UUIDField(label="Author UUID", required=False)

class PostAuthor(forms.Form):
    name = forms.CharField(label="Name", max_length=200, required=False)
    age = forms.IntegerField(label="Age", required=False)
    email = forms.EmailField(label="Email", required=False)

class BookForm(forms.ModelForm): 
    title = forms.CharField(
        label="Name",
        max_length=150,
        required=False,
        validators=[validators.RegexValidator(regex='^.{3,}$')],
        error_messages={'invalid':'Название книги слишком короткое'}
    )
    color = forms.CharField(label='Color', max_length=150, required=False)

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


    def clean(self):
        super().clean()
        errors = dict()
        if self.cleaned_data['description'] != 'book':
            errors['description'] = ValidationError('error desc')
        if self.cleaned_data['page_num'] != 100:
            errors['page_num'] = ValidationError('error page_num')
        if errors:
            raise ValidationError(errors)