# Generated by Django 4.2.1 on 2023-06-20 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_book_binding'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='description',
        ),
    ]
