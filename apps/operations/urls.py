from django.conf.urls import url,include
from django.urls import path
from .views import *


app_name = '[operations]'
urlpatterns = [
    # 收藏夹列表
    path(r'favorlist/',FavorListView.as_view(),name='favorlist'),
    # 添加收藏
    path(r'favorcreate/',FavorCreateView.as_view(),name='favorcreate'),
    # 取消收藏
    path(r'favordelete/<int:pk>/',FavorDeleteView.as_view(),name='favordelete'),
    # 获取单条数据详情
    path(r'favordetail/<int:pk>/',FavorDetailView.as_view(),name='favordetail'),
    path(r'favorupdate/<int:pk>/',FavorUpdateView.as_view(),name='favorupdate'),
    path(r'cartlist/',CartListView.as_view(),name='cartlist'),
    path(r'cartcreate/',CartCreateView.as_view(),name='cartcreate'),
    path(r'cartdelete/<int:pk>/',CartDeleteView.as_view(),name='cartdelete'),
    path(r'cartupdate/<int:pk>/',CartUpdateView.as_view(),name='cartupdate'),
    path(r'cartdetail/<int:pk>/',CartDetailView.as_view(),name='cartdetail'),

]