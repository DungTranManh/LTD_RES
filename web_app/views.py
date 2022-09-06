from django.shortcuts import render,HttpResponse
from .models import Data
from django.db.models import Q
# Create your views here.


def index(request):
    return render(request, 'web_app/home.html')


def NhaHang(request):
    return render(request, 'web_app/nhahang.html')


def KhuyenMai(request):
    get_data = Data.objects.filter(YN_Sale = '1')
    return render(request, 'web_app/khuyenmai.html',{'datas': get_data})

def SanPham(request):
    return render(request, 'web_app/sanpham.html')