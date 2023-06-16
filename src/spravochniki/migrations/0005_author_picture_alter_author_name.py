# Generated by Django 4.2.1 on 2023-06-13 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spravochniki', '0004_series'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='picture',
            field=models.ImageField(default='-', upload_to='uploads/%Y/%m/%d/', verbose_name='Author picture'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(help_text='Pls, add name!', max_length=50, verbose_name='Name author'),
        ),
    ]