# Generated by Django 4.2.1 on 2023-06-20 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_alter_book_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='age_restrictions',
            field=models.IntegerField(blank=True, null=True, verbose_name='Age restrictions'),
        ),
        migrations.AlterField(
            model_name='book',
            name='weight',
            field=models.IntegerField(blank=True, null=True, verbose_name='Weight book (g)'),
        ),
    ]
