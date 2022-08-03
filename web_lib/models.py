import email
from enum import unique
from itertools import product
from tabnanny import verbose
from tkinter import CASCADE
import uuid
from pyexpat import model
from django.db import models
from django.core import validators
from django.contrib.auth.models import User

class Author(models.Model):

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ["id"]
        unique_together = ["name", "age"]

    TYPES = (
        ('a','foreign'),
        ('b','russian'),
        ('c','other')
    )
    
    id = models.UUIDField(primary_key=True, db_index=True, default=uuid.uuid4)
    name = models.CharField(
        verbose_name="Имя",
        max_length=200,
        validators=[validators.RegexValidator(regex='^.*em$', message="Wrong")]
        )
    age = models.PositiveIntegerField(verbose_name="Возраст автора")
    email = models.EmailField(verbose_name="Электронная почта", null=True, blank=True)
    lit_type = models.CharField(verbose_name="Тип литературы", choices=TYPES, default="a", max_length=200)

    def __str__(self):
        return self.name

    def info(self):
        name = ('Name: %s' % self.name)
        age = ('Age: %s' % self.age)
        lit_type = ('lit_type: %s' % self.get_lit_type_display())
        return [name, age, lit_type]


class Book(models.Model):

    class Meta:
        get_latest_by = "publisherd"
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    title = models.CharField(max_length=200,verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    page_num = models.PositiveIntegerField(verbose_name="кол-во страниц")
    publisherd = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class ExtUser(models.Model):

    desc = models.CharField(max_length=200)
    is_logged = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete = models.SET_NULL, null=True)
    def __str__(self):
        return self.desc

class Product(models.Model):

    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Store(models.Model):
    
    name = models.CharField(max_length=200)
    products = models.ManyToManyField(Product, related_name='stores')
    def __str__(self):
        return self.name