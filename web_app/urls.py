import imp
from django.urls import path
from . import views
from .views import SearchAPIVIEW

app_name = 'web_app'
urlpatterns = [
    path('', views.index, name='home'),
    path('nhahang/', views.NhaHang, name='nhahang' ),
    path('khuyenmai/', views.KhuyenMai, name='khuyenmai'),
    path('sanpham/', views.SanPham, name='sanpham'),
    path('sanpham/<int:product_id>/', views.Detail, name='detail'),
    path('test/',views.test,name='test'),
    path('search/', views.SearchPage, name='searchpage'),
    path('search/<str:text_search>/', SearchAPIVIEW.as_view(), name = 'SearchAPIVIEW')
]