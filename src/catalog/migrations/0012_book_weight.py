# Generated by Django 4.2.1 on 2023-06-20 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_book_isbn'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='weight',
            field=models.DecimalField(decimal_places=0, default='1', max_digits=6, verbose_name='Weight book (g)'),
            preserve_default=False,
        ),
    ]