from django.shortcuts import render
from random import randint
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

from . import models


class HomePage(generic.TemplateView):
    template_name = "spravochniki/HomePage.html"


#Author
class AuthorView(generic.DetailView):
    model = models.Author  
  
class AuthorListView(generic.ListView):
    model = models.Author  
    paginate_by = 20
   
class AuthorAddView(generic.CreateView):
    model = models.Author 
    fields = [
        "name", "description"
        ]    

class AuthorUpdateView(generic.UpdateView):
    model = models.Author
    template_name = "spravochniki/author_form.html"
    fields = [
        "name", "description"
        ]    

class AuthorDeleteView(generic.DeleteView):
    model = models.Author
    template_name = "spravochniki/Delete-author.html"
    success_url = "/"




#Izdatelstvo
class IzdatelstvoView(generic.DetailView):
    model = models.Izdatelstvo  

class IzdatelstvoListView(generic.ListView):
    model = models.Izdatelstvo  
    paginate_by = 20    

class IzdatelstvoAddView(generic.CreateView):
    model = models.Izdatelstvo 
    fields = [
        "name", "description"
        ]        

class IzdatelstvoUpdateView(generic.UpdateView):
    model = models.Izdatelstvo
    template_name = "spravochniki/izdatelstvo_form.html"
    fields = [
        "name", "description"
        ]    

class IzdatelstvoDeleteView(generic.DeleteView):
    model = models.Izdatelstvo
    template_name = "spravochniki/izdatelstvo-delete.html"
    success_url = "/"    



#Zhanr    
class ZhanrView(generic.DetailView):
    model = models.Zhanr

class ZhanrListView(generic.ListView):
    model = models.Zhanr  
    paginate_by = 20    

class ZhanrAddView(generic.CreateView):
    model = models.Zhanr 
    fields = [
        "name", "description"
        ]          
    
class ZhanrUpdateView(generic.UpdateView):
    model = models.Zhanr
    template_name = "spravochniki/Zhanr_form.html"
    fields = [
        "name", "description"
        ]       

class ZhanrDeleteView(generic.DeleteView):
    model = models.Zhanr
    template_name = "spravochniki/zhanr-delete.html"
    success_url = "/"    


#Zhanr    
class SeriesView(generic.DetailView):
    model = models.Series

class SeriesListView(generic.ListView):
    model = models.Series  
    paginate_by = 20    

class SeriesAddView(generic.CreateView):
    model = models.Series 
    fields = [
        "name", "description"
        ]          
    
class SeriesUpdateView(generic.UpdateView):
    model = models.Series
    template_name = "spravochniki/Zhanr_form.html"
    fields = [
        "name", "description"
        ]       

class SeriesDeleteView(generic.DeleteView):
    model = models.Series
    template_name = "spravochniki/zhanr-delete.html"
    success_url = "/"    
