from rest_framework import serializers, validators
from .models import *




class ShopAddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShopAddress
        fields = "__all__"