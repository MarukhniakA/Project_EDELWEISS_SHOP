# Generated by Django 4.2.1 on 2023-06-20 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_book_the_year_publishing'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pages',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of pages'),
        ),
    ]
