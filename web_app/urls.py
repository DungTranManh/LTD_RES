from django.urls import path
from . import views

app_name = 'web_app'
urlpatterns = [
    path('', views.index, name='home'),
    path('nhahang/', views.NhaHang, name='nhahang' ),
    path('khuyenmai/', views.KhuyenMai, name='khuyenmai'),
    path('sanpham/', views.SanPham, name='sanpham'),
    path('sanpham/<str:name_product>/', views.Detail, name='detail')
]