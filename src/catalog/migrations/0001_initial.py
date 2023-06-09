# Generated by Django 4.2.1 on 2023-06-17 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='uploads/%Y/%m/%d/', verbose_name='Book picture')),
                ('name', models.CharField(help_text='Pls, add name!', max_length=50, verbose_name='Name book')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description book')),
            ],
        ),
    ]
