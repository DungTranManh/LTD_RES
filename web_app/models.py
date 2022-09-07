from django.db import models

# Create your models here.

class Data(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=True,blank=True)
    price = models.IntegerField(null = True,blank= True)
    describe = models.TextField(null = True, blank=True)
    YN_Sale = models.TextField()
    sale = models.IntegerField(default=0)
    appreciate = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ('id','name','price', 'describe', 'sale','appreciate')


