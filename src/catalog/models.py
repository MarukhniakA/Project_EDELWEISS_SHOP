from django.db import models
from django.urls import reverse_lazy

import spravochniki.models

class Book(models.Model):

    name = models.CharField(
        verbose_name='Name book',
        max_length=50,
        help_text="Pls, add name!"
    )

    picture = models.ImageField(
        verbose_name='Book picture',
        upload_to="uploads/%Y/%m/%d/"
        )

    price = models.DecimalField(
        verbose_name='Price book',
        max_digits=6,
        decimal_places=2
    )

    author = models.ForeignKey(
        spravochniki.models.Author,
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

    zhanr = models.ForeignKey(
        spravochniki.models.Zhanr,
        on_delete=models.PROTECT,
        null =True,
        blank=True
    )

    the_year_publishing = models.DateField(
        verbose_name='The year of publishing',
        null =True,
        blank=True
        )


    pages = models.IntegerField(
        verbose_name='Number of pages',
        null =True,
        blank=True
    )

    binding = models.CharField(
        verbose_name='Binding book',
        max_length=50,
        null =True,
        blank=True
    )

    format = models.CharField(
        verbose_name='Format book',
        max_length=50,
        null =True,
        blank=True
    )    

    ISBN = models.CharField(
        verbose_name='ISBN',
        max_length=50,
        null =True,
        blank=True
    )

    weight = models.IntegerField(
        verbose_name='Weight book (g)',
        null =True,
        blank=True
    )

    age_restrictions = models.IntegerField(
        verbose_name='Age restrictions',
        null =True,
        blank=True
    )

    izdatelstvo = models.ForeignKey(
        spravochniki.models.Izdatelstvo,
        on_delete=models.PROTECT,
        null =True,
        blank=True
    )

    kolvo_book = models.DecimalField(
        verbose_name = 'Number of books available',
        max_digits = 6,
        decimal_places = 0
    )

    ACTIVE = (
        ('Active', 'Yes'),
        ('Not_active', 'No'),
    )
     
    active_book = models.CharField(
        verbose_name='Available for order',
        max_length=10,
        choices=ACTIVE
    )
    
    date_entry_catalog = models.DateField(
        verbose_name="Date of entry into the catalog",
        null =True,
        blank=True
    )

    date_of_change = models.DateField(
        verbose_name="Date of the last change of the card",
        null =True,
        blank=True
    )


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy('catalog:view-book', kwargs = {"pk": self.pk})
      