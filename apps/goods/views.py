from django.http import JsonResponse
from django.views import View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from goods.serializers import *
from .schemas import *
from .filters import *
# Create your views here.
# class GoodsListView1(View):
#     def get(self,request):
#         goodslist = Goods.objects.all()
#         goods = []
#         for good in goodslist:
#             goodsdict = {}
#             goodsdict['name'] = good.name
#             goodsdict['actual_price'] = good.actual_price
#             goods.append(goodsdict)
#         goodslist_json = json.dumps(goods)
#         return HttpResponse(goodslist_json)
#
#
#         goodslist = Goods.objects.values()
#         goodslist = list(goodslist)
#         for good in goodslist:
#             good['image'] = str(good['image'])
#             good['created_time'] = str(good['created_time'])
#         goodslist_json = json.dumps(goods)
#         return HttpResponse(goodslist_json)


class GoodsListView2(View):
    def get(self, request):
        # goodslist = Goods.objects.all()
        # goods = []
        # for good in goodslist:
        #     goodsdict = {}
        #     goodsdict['name'] = good.name
        #     goodsdict['actual_price'] = good.actual_price
        #     goods.append(goodsdict)
        # goodslist_json = json.dumps(goods)


        goodslist = Goods.objects.values()
        goodslist = list(goodslist)
        for good in goodslist:
            good['image'] = str(good['image'])
            good['created_time'] = str(good['created_time'])

        return JsonResponse(goodslist,safe=False)

class GoodsListView3(APIView):
    """
    商品列表页
    """

    def get(self, request):
        goodslist = Goods.objects.all()
        # 采用序列化器
        serializers_json = GoodsListSerializer(goodslist,many=True)
        return Response(serializers_json.data)

from rest_framework import mixins
from rest_framework import generics

class GoodsListView4(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class GoodsPagination(PageNumberPagination):
    page_size = 100 #每页显示的条数
    page_size_query_param = 'page_size'
    max_page_size = 1000
    page_query_param = 'p' #分页参数变量名


# 使用ListAPIView
class GoodsListView(generics.ListAPIView):
    """商品列表   +   商品详情"""
    queryset = Goods.objects.all() # 查询结果集设置
    serializer_class = GoodsListSerializer# 序列化器的设置
    pagination_class = GoodsPagination # 不指定就采用默认自带的分页器 采用全局配置
    schema = GoodListSchema #指定所采用的schema
    # permission_classes = (IsAuthenticated,) # 权限认证配置
    permission_classes =()
    #过滤器使用
    filter_backends = (DjangoFilterBackend,SearchFilter,OrderingFilter)
    filter_fields = ('name','detail')# 完全匹配
    search_fields = ('name','detail') # 模糊查询 搜索
    ordering_fields = ('sale_nums','actual_price') # 默认价格升序排列

    # 自定义过滤器
    filter_class = GoodsFilter



    #  过滤
    def get_queryset(self):
        # self.request.data:POST/GET/FILES/PUT/patch  表单（schema_form） self.request.data.get('id','')
        # self.request.query_params:GET  error:url:detail/<int:id> yes:?id=1
        #http: //127.0.0.1:8000/goods/list/?page =1 yes   schema_query
        # http: //127.0.0.1:8000/goods/detail/23  no
        print('path',self.request.path)# 获取请求路径
        #print(self.kwargs) 获取url里的参数值  schema_url
        good_id =self.request.query_params.get('good_id','')
        if good_id:

            queryset = Goods.objects.filter(pk=good_id) # 获取具体商品的信息
        else:
            queryset = Goods.objects.all()
        return  queryset


# 商品分类列表
class GoodsTypeView(generics.ListAPIView):
    queryset = GoodsType.objects.all()
    serializer_class = GoodsTypeSerializer3
    # 不需要分页
    schema = GoodTypeSchema
    pagination_class = None

    def get_queryset(self):
        type_id = self.request.query_params.get('type_id','')
        if type_id:
            queryset = GoodsType.objects.filter(id=type_id)
        else:
            queryset = GoodsType.objects.all()

        return queryset

# 商品展示图

