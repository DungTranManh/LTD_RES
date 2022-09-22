
from django.contrib import admin
from django.db import models
from .models import Data
from django.forms import Textarea
# Register your models here.


class DataAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': Textarea(
                       attrs={'rows': 3,
                              'cols': 30})},
    }
    list_display = ('id','name','image','price', 'unit', 'describe', 'YN_Sale','sale','appreciate','featured')
    list_editable = ('name','price','image','unit', 'describe','YN_Sale', 'sale','appreciate','featured')
    list_per_page = 9
admin.site.register(Data,DataAdmin)