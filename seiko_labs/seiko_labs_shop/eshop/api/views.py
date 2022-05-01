from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from ..models import Product, Shop, Category
from .serializers import ProductSerializer, ShopSerializer, CategorySerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        shop_id = self.kwargs.get('shop_id')
        category_id = self.kwargs.get('category_id')
        print(self.kwargs)
        if shop_id and category_id:
            queryset = queryset.filter(category_id=category_id, category__shop_id=shop_id)
        return queryset


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ShopDetailView(generics.ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class CategoryDetailView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class ProductEnrollView(APIView):
#     def post(self, request, pk, format=None):
#         product = get_object_or_404(Product, pk=pk)
#         product.name.add(request.user)
#         return Response({'enrolled': True})