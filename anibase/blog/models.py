from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Artwork(models.Model):
    SEASON_CHOICES = [('w', 'Зима/Winter'),
                      ('s', 'Вестна/Spring'),
                      ('a', 'Осень/Autumn'),
                      ('s', 'Лето/Summer'),
                      ('n', 'None')
                      ]

    """Название"""
    title = models.CharField(max_length=256, verbose_name='Название')
    english_title = models.CharField(max_length=256, verbose_name='Англиское название', blank=True, null=True)
    alternative_title = models.ManyToManyField('AlternativeName', verbose_name='Альтернативные названия', blank=True)

    """Пренадлежит серии книг/сериалов/..."""
    series = models.ForeignKey('SeriesArtwork', on_delete=models.PROTECT)
    series_number = models.IntegerField(verbose_name="Номер тома или сезона", null=True, blank=True, default=1)

    """Обложка"""
    image = models.ImageField(upload_to="artwork_covers/%Y/", verbose_name='Обложка', null=True, blank=True)

    """Количество глав в книге/ серий в сериале"""
    episodes = models.IntegerField(verbose_name="Количество глав/серий", default=12)

    """К какой категории принадлежит работа, книга/сериал/новела/..."""
    category = models.ManyToManyField('CategoryArtwork', verbose_name='Категория')

    """Год и сезоне когда вышло произведение зима/вестна/лето/осень"""
    year = models.IntegerField(verbose_name="Год", blank=True, null=True)
    year_season = models.CharField(max_length=1, choices=SEASON_CHOICES, default='n')

    """Оценка и описание"""
    rating = models.IntegerField(verbose_name="Оценка", blank=True, null=True)
    description = models.TextField(blank=True, verbose_name="Описание")

    """Автор"""
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, verbose_name='Автор', blank=True, null=True)

    """Пользовательские данные"""
    creator = models.ManyToManyField(User, verbose_name='Автор записи')
    viewing_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата просмотра', blank=True)
    create_data = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи", blank=True)

    slug = models.SlugField(verbose_name="URL", unique=True, db_index=True, blank=True)
    is_active = models.BooleanField(default=True)

    type_artwork = models.ForeignKey('TypeArtwork', on_delete=models.PROTECT, verbose_name="Тип произведения", blank=True, null=True)

    class Meta:
        ordering = ['-viewing_date']

    def __str__(self):
        return self.title


class AlternativeName (models.Model):
    title = models.CharField(max_length=256, verbose_name='Альтернативное название')

    def __str__(self):
        return self.title


class CategoryArtwork (models.Model):
    name = models.CharField(max_length=256, verbose_name="Название")

    def __str__(self):
        return self.name


class SeriesArtwork(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=256, verbose_name="Имя/Псевданим")

    def __str__(self):
        return self.name


class TypeArtwork(models.Model):
    title = models.CharField(max_length=256, verbose_name="Название типа произведения")

    def __str__(self):
        return self.title
