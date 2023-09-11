# Generated by Django 4.2.5 on 2023-09-11 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AlternativeName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Альтернативное название')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Имя/Псевданим')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryArtwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='SeriesArtwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='TypeArtwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название типа произведения')),
            ],
        ),
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('english_title', models.CharField(blank=True, max_length=256, null=True, verbose_name='Англиское название')),
                ('series_number', models.IntegerField(blank=True, default=1, null=True, verbose_name='Номер тома или сезона')),
                ('image', models.ImageField(blank=True, null=True, upload_to='artwork_covers/%Y/', verbose_name='Обложка')),
                ('episodes', models.IntegerField(default=12, verbose_name='Количество глав/серий')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='Год')),
                ('year_season', models.CharField(choices=[('w', 'Зима/Winter'), ('s', 'Вестна/Spring'), ('a', 'Осень/Autumn'), ('s', 'Лето/Summer'), ('n', 'None')], default='n', max_length=1)),
                ('rating', models.IntegerField(blank=True, null=True, verbose_name='Оценка')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('viewing_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата просмотра')),
                ('create_data', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='URL')),
                ('is_active', models.BooleanField(default=True)),
                ('alternative_title', models.ManyToManyField(blank=True, to='blog.alternativename', verbose_name='Альтернативные названия')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.author', verbose_name='Автор')),
                ('category', models.ManyToManyField(to='blog.categoryartwork', verbose_name='Категория')),
                ('creator', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Автор записи')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.seriesartwork')),
                ('type_artwork', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.typeartwork', verbose_name='Тип произведения')),
            ],
            options={
                'ordering': ['-viewing_date'],
            },
        ),
    ]
