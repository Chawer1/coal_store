# Generated by Django 3.1.3 on 2020-11-17 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='for_anonymous_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cart',
            name='in_order',
            field=models.BooleanField(default=False),
        ),
    ]
