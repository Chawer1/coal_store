# Generated by Django 3.1.3 on 2020-11-21 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniapp', '0004_auto_20201121_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coal',
            name='burning_time',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Время горения'),
        ),
        migrations.AlterField(
            model_name='coal',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер телефона'),
        ),
    ]
