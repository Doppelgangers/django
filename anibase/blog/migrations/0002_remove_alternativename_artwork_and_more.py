# Generated by Django 4.2.5 on 2023-09-10 18:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alternativename',
            name='artwork',
        ),
        migrations.AddField(
            model_name='artwork',
            name='alternative_title',
            field=models.ManyToManyField(to='blog.alternativename', verbose_name='Англиское название'),
        ),
        migrations.RemoveField(
            model_name='artwork',
            name='creator',
        ),
        migrations.AlterField(
            model_name='artwork',
            name='english_title',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Англиское название'),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='episodes',
            field=models.IntegerField(default=12, verbose_name='Количество глав/серий'),
        ),
        migrations.AddField(
            model_name='artwork',
            name='creator',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL, verbose_name='Автор записи'),
        ),
    ]
