from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import mixins
from .models import *
from .serializers import FavorSerializers,ShopCartSerializers
from users.views import IsOwnerOrReadOnly

# Create your views here.


# 收藏夹列表

class FavorListView1(generics.ListAPIView):
    queryset = Favor.objects.all()
    serializer_class = FavorSerializers
    # 过滤返回当前用户的收藏夹信息
    def get_queryset(self):
        queryset = Favor.objects.filter(user=self.request.user)
        return queryset


class FavorListView(generics.ListAPIView):
    queryset = Favor.objects.all()
    serializer_class = FavorSerializers
    # 过滤返回当前用户的收藏夹信息
    def get_queryset(self):
        return super().get_queryset().filter(user = self.request.user)


# 加入收藏夹 -- 新增
class FavorCreateView(generics.CreateAPIView):
    serializer_class = FavorSerializers
    # 自定义返回结果
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try: # 失败信息的定制
            serializer.is_valid(raise_exception=True)
        except:
            return Response(data={'code':400,'message':'收藏失败'},status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        res = Response(serializer.data, status=status.HTTP_200_OK, headers=headers)
        # 成功后返回信息的定制
        res.data['code'] = 200
        res.data['message'] = '收藏成功'
        return res

# 取消收藏 --删除 - delete
class FavorDeleteView1(generics.DestroyAPIView):
    queryset = Favor.objects.all()
    serializer_class = FavorSerializers
    permission_classes = (IsOwnerOrReadOnly,)
    # 重写destory方法 ，自定义返回结果
    def destroy(self, request, *args, **kwargs):
        #自定义失败返回信息
        try:
            instance = self.get_object()
        except:
            return Response(data={'code':400,'message':'取消失败'},status = status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(instance)
        return Response(data={'code':200,'message':'取消成功'},status=status.HTTP_204_NO_CONTENT)



# 取消收藏 --删除 get
class FavorDeleteView(generics.GenericAPIView):
    queryset = Favor.objects.all()
    serializer_class = FavorSerializers
    permission_classes = (IsOwnerOrReadOnly,)
    # 重写destory方法 ，自定义返回结果
    def get(self,request,pk):
        # 获取地址url中的参数
        try:
            obj = Favor.objects.get(pk=pk)
            self.check_object_permissions(request,obj)
            Favor.objects.get(pk=pk).delete() # 使用get获取单条数据 ,使用filter会获取一个列表 列表为空不会报错
        except:
            return Response(data={'code':400,'message':'删除失败'},status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'code':200,'message':'删除成功'},status=status.HTTP_200_OK)


# 获取单条数据详情
class FavorDetailView(generics.RetrieveAPIView):
    queryset = Favor.objects.all()
    serializer_class = FavorSerializers

# 修改 - - put  patch
class FavorUpdateView1(generics.UpdateAPIView):
    queryset = Favor.objects.all()
    serializer_class = FavorSerializers
    # put 接口   整体修改（一条数据整体修改）
    # patch 接口  局部修改(一条数据中的某列值）

class FavorUpdateView(generics.GenericAPIView,mixins.UpdateModelMixin):
    queryset = Favor.objects.all()
    serializer_class = FavorSerializers
    # 数据编辑post方式
    def post(self,request,pk,*args,**kwargs):
        # print('request:',request)
        # print('**kwargs',kwargs)
        # 调用updateModelMixin中的update方法
        try:
            self.update(request,*args,**kwargs)
        except:
            return Response(data={'code':400,'message':'修改失败'},status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'code':200,'message':'修改成功'},status=status.HTTP_200_OK)



class CartListView(generics.ListAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShopCartSerializers
    def get_queryset(self):
        queryset = ShoppingCart.objects.filter(user = self.request.user)
        return queryset


class CartCreateView(generics.CreateAPIView):
    serializer_class = ShopCartSerializers
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try: # 失败信息的定制
            serializer.is_valid(raise_exception=True)
        except:
            return Response(data={'code':400,'message':'添加失败'},status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        res = Response(serializer.data, status=status.HTTP_200_OK, headers=headers)
        # 成功后返回信息的定制
        res.data['code'] = 200
        res.data['message'] = '添加成功'
        return res

class CartDeleteView(generics.GenericAPIView):
    """

    """
    queryset = ShoppingCart.objects.all()
    serializer_class = ShopCartSerializers
    def get(self,request,pk):
        try:
            ShoppingCart.objects.get(pk=pk).delete()
        except:
            return Response(data={
                'code':400,
                'message':'删除失败',
            },status=status.HTTP_400_BAD_REQUEST)
        return Response(data={
            'code':200,
            'message':'删除成功'
        },status=status.HTTP_200_OK)


class CartDetailView(generics.RetrieveAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShopCartSerializers

class CartUpdateView(generics.GenericAPIView,mixins.UpdateModelMixin):
    """

    """
    queryset = ShoppingCart.objects.all()
    serializer_class = ShopCartSerializers
    def post(self,request,pk,*args,**kwargs):
        try:
            self.update(request,*args,**kwargs)
        except:

            return Response(data={
                'code':400,
                'message':'修改失败',
            },status=status.HTTP_400_BAD_REQUEST)

        return Response(data={
                'code':200,
                'message':'修改成功',
            },status=status.HTTP_200_OK)

