from django.shortcuts import render
from products.models import Product
from .serializers import ProductSerializer

# Create your views here.

class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer