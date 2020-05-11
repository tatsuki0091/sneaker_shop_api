from django.shortcuts import render
from products.models import Product
from django.views.generic import View
from .serializers import ProductSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.generics import (
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    )
from rest_framework.response import Response
from django.http import HttpResponse
from django.core import serializers

CROUSEL_NUM = 5

# 一覧を表示
class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all().order_by('-published_date')
    serializer_class = ProductSerializer

class GetInfoForCrouselAPIView(generics.ListAPIView):
    queryset = Product.objects.all().order_by('?')[:CROUSEL_NUM]
    serializer_class = ProductSerializer

# 検索結果を表示
class SearchProductsAPIView(APIView):

    def get(self, request):
        # リクエストから値を取得
        name = request.GET.get("name") 
        # リクエストを元に該当するデータを検索
        queryset = Product.objects.filter(name__icontains=name)

        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

        
# 詳細画面の結果を返す
class ProductDetailAPIView(RetrieveAPIView):
    lookup_field = 'id'
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer