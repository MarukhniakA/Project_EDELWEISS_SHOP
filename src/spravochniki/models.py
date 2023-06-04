from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(
        verbose_name='Name author',
        max_length=50
    )
    description = models.TextField(
        verbose_name='Description author',
        null =True,
        blank=True
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f"/author-cbv/{self.pk}"
    

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
        return f"/izdatelstvo-cbv/{self.pk}"
 

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
        return f"/zhanr-cbv/{self.pk}"
 
 
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
        return f"/series-cbv/{self.pk}"