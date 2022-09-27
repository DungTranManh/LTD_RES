from operator import ge
from webbrowser import get
from django.shortcuts import render,HttpResponse
from .models import Data
from django.db.models import Q
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