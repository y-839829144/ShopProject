from django.contrib.auth.backends import ModelBackend
from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework import mixins
from .models import *
from .serializers import ShopAddressSerializers
from django.db.models import Q
from django.contrib.auth.models import User
# Create your views here.



class ShopAddressListView(generics.ListAPIView):
    queryset = ShopAddress.objects.all()
    serializer_class = ShopAddressSerializers
    # 过滤返回当前用户的收货地址
    def get_queryset(self):
        queryset = ShopAddress.objects.filter(user=self.request.user)
        return queryset

class ShopAddressListView1(generics.GenericAPIView):
    queryset = ShopAddress.objects.all()
    serializer_class = ShopAddressSerializers

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)



class ShopAddressCreateView(generics.CreateAPIView):
    serializer_class = ShopAddressSerializers
    # 自定义返回结果
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
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




class ShopAddressDeleteView(generics.GenericAPIView):
    queryset = ShopAddress.objects.all()
    serializer_class = ShopAddressSerializers
    # 重写destory方法 ，自定义返回结果
    def get(self,request,pk):
        # 获取地址url中的参数
        try:
            ShopAddress.objects.get(pk=pk).delete() # 使用get获取单条数据 ,使用filter会获取一个列表 列表为空不会报错
        except:
            return Response(data={'code':400,'message':'删除失败'},status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'code':200,'message':'删除成功'},status=status.HTTP_200_OK)



class ShopAddressUpdateView(generics.GenericAPIView,mixins.UpdateModelMixin):
    queryset = ShopAddress.objects.all()
    serializer_class = ShopAddressSerializers

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





def jwt_response_payload_handler(token,user=None,request=None):
    # 通过用户user对象即可获取用户相关权限等其他信息
    return {
        'token':token,
        'user':user.username,
        'test':'test',
    }
# 自定义登陆验证
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except:
            return None

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    自定义权限只允许对象的所有者编辑它。
    """
    def has_object_permission(self, request, view, obj):
        # 读取权限被允许用于任何请求，
        # 所以我们始终允许 GET，HEAD 或 OPTIONS 请求。
        # if request.method in permissions.SAFE_METHODS:
        #     return True

        # 写入权限只允许给 snippet 的所有者。
        return obj.user == request.user