from django.shortcuts import render
from products.models import Product
from .serializers import ProductSerializer
from rest_framework import generics
from rest_framework.generics import (
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    )

# Create your views here.

# 一覧を表示
class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all().order_by('-published_date')
    serializer_class = ProductSerializer

# 詳細画面の結果を返す
class ProductDetailAPIView(RetrieveAPIView):
    lookup_field = 'id'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer