
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
    list_display = ('id','name','price', 'describe', 'sale','appreciate')
    list_editable = ('name','price', 'describe', 'sale','appreciate')
    list_per_page = 9
admin.site.register(Data,DataAdmin)