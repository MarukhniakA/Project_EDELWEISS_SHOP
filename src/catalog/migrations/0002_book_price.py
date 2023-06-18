# Generated by Django 4.2.1 on 2023-06-17 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=0, default='1', max_digits=6, verbose_name='Price book'),
            preserve_default=False,
        ),
    ]
