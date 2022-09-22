from django.db import models

# Create your models here.

class Data(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=True,blank=True)
    image = models.TextField(blank=True)
    price = models.TextField(null = True,blank= True)
    unit = models.TextField(null = True, blank=True)
    describe = models.TextField(null = True, blank=True)
    YN_Sale = models.BooleanField(default=False, null= False)
    sale = models.IntegerField(default=0)
    appreciate = models.FloatField(null=True, blank=True)
    featured = models.BooleanField(null=True, default=False)

    class Meta:
        ordering = ('id','name','image','price', 'unit', 'describe', 'sale','appreciate','featured')


