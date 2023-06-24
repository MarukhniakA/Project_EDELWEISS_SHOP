from django.db import models
from django.urls import reverse_lazy
# Create your models here.

class Author(models.Model):

    name = models.CharField(
        verbose_name='Name author',
        max_length=50,
        help_text="Pls, add name!"
    )
    description = models.TextField(
        verbose_name='Description author',
        null =True,
        blank=True
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy('spravochniki:view-author', kwargs = {"pk": self.pk})
      
       
     

class Izdatelstvo(models.Model):
    
    name = models.CharField(
        verbose_name='Name izdatelstvo',
        max_length=50
    )
    description = models.TextField(
        verbose_name='Description izdatelstvo',
        null =True,
        blank=True
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy('spravochniki:view-izdatelstvo', kwargs = {"pk": self.pk})
    
 

class Zhanr(models.Model):
    
    name = models.CharField(
        verbose_name='Name zhanr',
        max_length=50
    )
    description = models.TextField(
        verbose_name='Description zhanr',
        null =True,
        blank=True
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy('spravochniki:view-zhanr', kwargs = {"pk": self.pk})
 
 
 
class Series(models.Model):
    
    name = models.CharField(
        verbose_name='Name series book',
        max_length=50
    )
    description = models.TextField(
        verbose_name='Description series book',
        null =True,
        blank=True
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy('spravochniki:view-series', kwargs = {"pk": self.pk})
       

class Status(models.Model):

    name = models.CharField(
        verbose_name='Name status',
        max_length=50
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy('spravochniki:view-status', kwargs = {"pk": self.pk})