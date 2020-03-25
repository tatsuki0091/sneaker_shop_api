from django.shortcuts import render
from products.models import Product
from .serializers import ProductSerializer
from rest_framework import generics

# Create your views here.

class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all().order_by('-published_date')
    serializer_class = ProductSerializer

class ProductDetailAPIView(generics.ListAPIView):
    id=1
    queryset = Product.objects.filter(id=id)
    print(queryset)
    serializer_class = ProductSerializer