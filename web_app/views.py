from django.shortcuts import render,HttpResponse
from .models import Data
from django.db.models import Q
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SearchSerializer
# Create your views here.


def index(request):
    get_data = Data.objects.filter(featured = True)
    return render(request, 'web_app/home.html', {'datas': get_data})


def NhaHang(request):
    return render(request, 'web_app/nhahang.html')


def KhuyenMai(request):
    get_data = Data.objects.filter(YN_Sale = True)
    return render(request, 'web_app/khuyenmai.html',{'datas': get_data})

def SanPham(request):
    get_all_data = Data.objects.all()
    return render(request, 'web_app/sanpham.html', {'datas': get_all_data})

def Detail(request,product_id):
    get_product = Data.objects.get(id=product_id)
    return render(request, 'web_app/detail.html',{'product': get_product})


def SearchPage(request):
    return render(request, 'web_app/search.html')

class SearchAPIVIEW(APIView):
    def get(self,request,text_search):
        data_get = Data.objects.filter(name__contains=text_search)
        if not data_get:
            return Response(data='can not get data', status=status.HTTP_404_NOT_FOUND)
        else:
            data_get_serializer = SearchSerializer(data_get, many=True)
            return Response(data=data_get_serializer.data, status=status.HTTP_200_OK)
