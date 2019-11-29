from rest_framework import serializers, validators
from .models import *

class FavorSerializers(serializers.ModelSerializer):
    # 隐藏user字段，并且赋值为当前登录用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Favor
        fields = "__all__"
        # fields = ('user','goods')
        extra_kwargs = { # 对模型已有参数重新设置和编辑
            'created_time':{'required':False,'read_only':True}# 可以不填   read_only 不显示该字段
        }
        # 收藏夹 用户和商品的联合唯一限制（验证器）
        validators = [
            validators.UniqueTogetherValidator(
                queryset= Favor.objects.all(),
                fields = ("user","goods"),
                message= "该商品已收藏，请勿重复收藏！"
            )
        ]
class ShopCartSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = ShoppingCart
        fields = "__all__"
        extra_kwargs = {
            'created_time':{'required':False,'read_only':True}
        }
        validators.UniqueTogetherValidator(
            queryset=ShoppingCart.objects.all(),
            fields = ("user"),
            message= None
        )
