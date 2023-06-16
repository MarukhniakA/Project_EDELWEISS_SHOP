from django.shortcuts import render
from random import randint
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy

from . import models
from pathlib import Path

from PIL import Image

def resizer(image):
    extention = image.file.name.split('.')[-1]
    BASE_DIR = Path(image.file.name).resolve().parent
    file_name = Path(image.file.name).resolve().name.split('.')
    for m_basewidth in [150, 40]:
        #m_basewidth = 150
        im = Image.open(image.file.name)
        wpercent = (m_basewidth/float(im.size[0]))
        hsize = int((float(im.size[1])*float(wpercent))) 
        im.thumbnail((m_basewidth, hsize), Image.Resampling.LANCZOS)
        im.save(str(BASE_DIR / "".join(file_name[:-1])) + f'_{m_basewidth}_.' + extention )
  

class HomePage(generic.TemplateView):
    template_name = "spravochniki/HomePage.html"


#Author
class AuthorView(generic.DetailView):
    model = models.Author  
  
class AuthorListView(LoginRequiredMixin, generic.ListView):
    login_url = reverse_lazy("staff:login")
    model = models.Author  
    paginate_by = 20
   
class AuthorAddView(generic.CreateView):
    model = models.Author 
    fields = [
       "picture", "name", "description"
        ]    
    
    def get_success_url(self) -> str:
        resizer(self.object.picture)
        return super().get_success_url()

class AuthorUpdateView(generic.UpdateView):
    model = models.Author
    template_name = "spravochniki/author_form.html"
    fields = [
        "picture", "name", "description"
        ]    

class AuthorDeleteView(generic.DeleteView):
    model = models.Author
    template_name = "spravochniki/Delete-author.html"
    success_url = "/"




#Izdatelstvo
class IzdatelstvoView(generic.DetailView):
    model = models.Izdatelstvo  

class IzdatelstvoListView(generic.ListView):
    login_url = reverse_lazy("staff:login")
    model = models.Izdatelstvo  
    paginate_by = 20    

class IzdatelstvoAddView(generic.CreateView):
    model = models.Izdatelstvo 
    fields = [
        "picture", "name", "description"
        ]        
    
    def get_success_url(self) -> str:
        resizer(self.object.picture)
        return super().get_success_url()

class IzdatelstvoUpdateView(generic.UpdateView):
    model = models.Izdatelstvo
    template_name = "spravochniki/izdatelstvo_form.html"
    fields = [
        "picture", "name", "description"
        ]    
    

class IzdatelstvoDeleteView(generic.DeleteView):
    model = models.Izdatelstvo
    template_name = "spravochniki/izdatelstvo-delete.html"
    success_url = "/"    



#Zhanr    
class ZhanrView(generic.DetailView):
    model = models.Zhanr

class ZhanrListView(generic.ListView):
    login_url = reverse_lazy("staff:login")
    model = models.Zhanr  
    paginate_by = 20    

class ZhanrAddView(generic.CreateView):
    model = models.Zhanr 
    fields = [
        "picture", "name", "description"
        ]         

    def get_success_url(self) -> str:
        resizer(self.object.picture)
        return super().get_success_url() 
    
class ZhanrUpdateView(generic.UpdateView):
    model = models.Zhanr
    template_name = "spravochniki/Zhanr_form.html"
    fields = [
        "picture", "name", "description"
        ]       

class ZhanrDeleteView(generic.DeleteView):
    model = models.Zhanr
    template_name = "spravochniki/zhanr-delete.html"
    success_url = "/"    


#Series    
class SeriesView(generic.DetailView):
    model = models.Series

class SeriesListView(generic.ListView):
    login_url = reverse_lazy("staff:login")
    model = models.Series  
    paginate_by = 20    

class SeriesAddView(generic.CreateView):
    model = models.Series 
    fields = [
        "picture", "name", "description"
        ]          
    
    def get_success_url(self) -> str:
        resizer(self.object.picture)
        return super().get_success_url()

class SeriesUpdateView(generic.UpdateView):
    model = models.Series
    template_name = "spravochniki/Zhanr_form.html"
    fields = [
        "picture", "name", "description"
        ]       

class SeriesDeleteView(generic.DeleteView):
    model = models.Series
    template_name = "spravochniki/zhanr-delete.html"
    success_url = "/"    


