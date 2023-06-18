from django.db import models
from django.urls import reverse_lazy

import spravochniki.models

class Book(models.Model):

    picture = models.ImageField(
        verbose_name='Book picture',
        upload_to="uploads/%Y/%m/%d/"
        )

    name = models.CharField(
        verbose_name='Name book',
        max_length=50,
        help_text="Pls, add name!"
    )

    author = models.ForeignKey(
        spravochniki.models.Author,
        on_delete=models.PROTECT,
        null =True,
        blank=True
    )
    
    zhanr = models.ForeignKey(
        spravochniki.models.Zhanr,
        on_delete=models.PROTECT,
        null =True,
        blank=True
    )

    series = models.ForeignKey(
        spravochniki.models.Series,
        on_delete=models.PROTECT,
        null =True,
        blank=True
    )

    izdatelstvo = models.ForeignKey(
        spravochniki.models.Izdatelstvo,
        on_delete=models.PROTECT,
        null =True,
        blank=True
    )

    description = models.TextField(
        verbose_name='Description book',
        null =True,
        blank=True
    )

    price = models.DecimalField(
        verbose_name='Price book',
        max_digits=6,
        decimal_places=0
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy('catalog:view-book', kwargs = {"pk": self.pk})
      