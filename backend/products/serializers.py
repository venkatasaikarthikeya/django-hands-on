from rest_framework import serializers
from products.models import Product

"""
Serializer:
1. It can easily do the model_to_dict stuff with the flexibility to add properties and methods to the response
2. It can be used to enrich the Model class 
"""


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

    # obj is the actual instance of product that serializer is currently dealing with
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()