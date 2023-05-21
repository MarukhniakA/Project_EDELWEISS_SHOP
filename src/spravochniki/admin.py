from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.Author)
admin.site.register(models.Izdatelstvo)
admin.site.register(models.Zhanr)
admin.site.register(models.Series)