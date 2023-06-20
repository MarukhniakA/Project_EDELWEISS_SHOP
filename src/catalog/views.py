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
  

#class HomePage(generic.TemplateView):
#    template_name = "home/HomePage.html"


#Author
class BookView(generic.DetailView):
    model = models.Book  
  
class BookListView(LoginRequiredMixin, generic.ListView):
    login_url = reverse_lazy("staff:login")
    model = models.Book  
    paginate_by = 20
   
class BookAddView(generic.CreateView):
    model = models.Book 
    fields = [
       "picture", "name", "price", "author", "series",  "zhanr", "the_year_publishing", "pages", "binding", "format", "ISBN", "weight", "age_restrictions", "izdatelstvo", "kolvo_book", "active_book", "date_entry_catalog", "date_of_change"
        ]    
    
    def get_success_url(self) -> str:
        resizer(self.object.picture)
        return super().get_success_url()

class BookUpdateView(generic.UpdateView):
    model = models.Book
    template_name = "catalog/book_form.html"
    fields = [
        "picture", "name", "price", "author", "series",  "zhanr", "the_year_publishing", "pages", "binding", "format", "ISBN", "weight", "age_restrictions", "izdatelstvo", "kolvo_book", "active_book", "date_entry_catalog", "date_of_change"
        ]    

class BookDeleteView(generic.DeleteView):
    model = models.Book
    template_name = "catalog/Delete-book.html"
    success_url = "/"
