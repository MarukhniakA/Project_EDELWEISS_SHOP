# Generated by Django 4.2.1 on 2023-06-20 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_book_format_book_kolvo_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='active_book',
            field=models.CharField(choices=[('Y', 'active'), ('N', 'no_active')], default='1', max_length=6, verbose_name='Active/No_active book'),
            preserve_default=False,
        ),
    ]
