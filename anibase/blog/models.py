from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
# Create your models here.


class Artwork (models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    english_title = models.CharField(max_length=255, verbose_name='Англиское название', blank=True, null=True)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Обложка', null=True)
    year = models.IntegerField(verbose_name="Год", blank=True, null=True)
    rating = models.IntegerField(verbose_name="Оценка", blank=True, null=True)
    description = models.TextField(blank=True, verbose_name="Описание")

    number = models.IntegerField(verbose_name="Номер тома или сезона", null=True, blank=True)

    author = models.ForeignKey('Author', models.SET_NULL, verbose_name='Автор', blank=True, null=True)
    category = models.ForeignKey('Category', models.PROTECT, verbose_name='Категория')
    genre = models.ManyToManyField('Genre', verbose_name="Жанры", blank=True)
    series = models.ForeignKey('Series', models.PROTECT, verbose_name="Серия", blank=True, null=True)
    creator = models.ForeignKey(User, models.SET_NULL, verbose_name='Автор записи', blank=True, null=True)

    viewing_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата просмотра', blank=True)
    create_data = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации записи", blank=True)
    slug = models.SlugField(verbose_name="URL", unique=True, db_index=True, blank=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-viewing_date']


class Category (models.Model):
    title = models.CharField(max_length=255 , verbose_name='Название')
    slug = models.SlugField(verbose_name="URL", unique=True, db_index=True)


class Genre (models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(verbose_name="URL", unique=True, db_index=True)
    description = models.CharField(max_length=2_000, null=True, verbose_name="Описание")


class Series (models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(verbose_name="URL", unique=True, db_index=True)


class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя/Псевданим')
    slug = models.SlugField(verbose_name="URL", unique=True, db_index=True)
