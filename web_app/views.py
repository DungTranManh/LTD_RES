from django.shortcuts import render,HttpResponse
from .models import Data
from django.db.models import Q
# Create your views here.


def index(request):
    return render(request, 'web_app/home.html')


def NhaHang(request):
    return render(request, 'web_app/nhahang.html')


def KhuyenMai(request):
    get_data = Data.objects.filter(YN_Sale = True)
    return render(request, 'web_app/khuyenmai.html',{'datas': get_data})

def SanPham(request):
    return render(request, 'web_app/sanpham.html')

def Detail(request,name_product):
    get_product = Data.objects.get(name=name_product)
    return render(request, 'web_app/detail.html',{'product': get_product})