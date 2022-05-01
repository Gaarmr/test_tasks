from rest_framework import serializers
from ..models import Product, Shop, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ShopSerializer(serializers.ModelSerializer):
    categoryes = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Shop
        fields = ('id', 'name', 'categoryes')


class ProductSerializer(serializers.ModelSerializer):
    categoryes = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'update_counter', 'categoryes')





# from eshop.models import Product
# from eshop.api.serializers import ProductSerializer
# product = Product.objects.latest('id')
# serializer = ProductSerializer(product)
# serializer.data

# from io import BytesIO
# from rest_framework.parsers import JSONParser
# data = b'{"id":4,"title":"Music","slug":"music"}'
# JSONParser().parse(BytesIO(data))