from django.conf.urls import url
from goods import views
from django.urls import path

from goods.views import GoodsTypeView

app_name = '[goods]'
urlpatterns = [
   url(r'^list/', views.GoodsListView.as_view(), name='list'),
   path(r'typelist/',GoodsTypeView.as_view(),name='typelist'),

]