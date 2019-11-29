from django.conf.urls import url,include
from django.urls import path
from .views import *


app_name = '[users]'
urlpatterns = [
    #收货地址列表
    path(r'shopaddresslist/',ShopAddressListView.as_view(),name='shopaddresslist'),
    #增加收货地址
    path(r'shopaddresscreate/<int:pk>/',ShopAddressCreateView.as_view(),name='shopaddresscreate'),
    #删除收货地址
    path(r'shopaddressdelete/<int:pk>/',ShopAddressDeleteView.as_view(),name='shopaddressdelete'),
    #修改收货地址
    path(r'shopaddressupdate/<int:pk>/',ShopAddressUpdateView.as_view(),name='shopaddressupdate'),
]