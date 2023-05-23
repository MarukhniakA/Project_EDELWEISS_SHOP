from django.shortcuts import render
from random import randint
from django.http import HttpResponse

from . import models


#List
def home_page(request):
    authors = models.Author.objects.filter(pk__lt=15)
    return render(
        request, 
        template_name="spravochniki/home_page.html", 
        context={'key': authors})


#Read
def view_author(request, pk):
    author = models.Author.objects.get(pk=int(pk))
    return render(
        request, 
        template_name="spravochniki/view_author.html", 
        context={'key': author})


#Delete
def delete_author(request, pk):
    models.Author.objects.get(pk=int(pk)).delete()
    return HttpResponse(f"Object {pk} has been deleted!")


