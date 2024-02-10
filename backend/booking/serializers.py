from rest_framework import serializers

from .models import Item, Cart, Order 


class ItemSerializer(serializers.ModelSerializer):
    """
    Serializer class 
    """
    class Meta:
        model = Item
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    """
    Serializer class
    """
    class Meta:
        model = Cart
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    """
    Serializer class 
    """
    class Meta:
        model = Order
        fields = "__all__"
