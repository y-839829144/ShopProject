from rest_framework import serializers
from goods.models import Goods,GoodsType,GoodsDisplayFiles
# 商品列表序列化
class GoodsListSerializer1(serializers.Serializer):
    name = serializers.CharField(required=True)
    actual_price = serializers.IntegerField(required=True)

class GoodsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsType
        fields = "__all__"

class GoodsDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsDisplayFiles
        fields = "__all__"
# 商品信息
class GoodsListSerializer(serializers.ModelSerializer):
    one_typename = GoodsTypeSerializer()  # 一访问一（外表找主表）
    two_typename = GoodsTypeSerializer()
    three_typename = GoodsTypeSerializer()
    img = GoodsDisplaySerializer(many=True)    # related_name 一访问多 主表找外表
    class Meta:
        model = Goods
        # fields = ('name','actual_price')
        #全部
        fields = "__all__" # 包含
        # exclude = ('name',) # 不包含


# 商品分类信息
class GoodsTypeSerializer1(serializers.ModelSerializer):

    class Meta:
        model = GoodsType
        fields = "__all__"

class GoodsTypeSerializer2(serializers.ModelSerializer):
    sonm = GoodsTypeSerializer1(many=True)
    class Meta:
        model = GoodsType
        fields = "__all__"

class GoodsTypeSerializer3(serializers.ModelSerializer):
    sonm = GoodsTypeSerializer2(many=True) #  models 外键设置属性related_name=son
    class Meta:
        model = GoodsType
        fields = "__all__"
