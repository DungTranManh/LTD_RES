from dataclasses import fields
from rest_framework import serializers
from .models import Data


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['id','name','describe','image','price','unit','YN_Sale',]