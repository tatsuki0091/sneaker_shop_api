from django.shortcuts import render
from rest_framework import generics
from carts.models import Cart
from members.models import Member
from .serializers import AddToCartSerializer
from rest_framework.response import Response
import logging
from products.models import Product
from rest_framework import status

# Add to Cart
class AddToCartAPIView(generics.ListCreateAPIView):
    logfile = r"/Users/Tatsuki/projects/django/book_shop_api/book_shop_api/development.log"
    logging.basicConfig(filename=logfile, level=logging.DEBUG)
    def post(self, request, format=None, *args, **kwargs):

        # リクエストの値の存在判定
        if request.data['member_id'] is None:
            return Response(False, status=status.HTTP_200_OK)
        if request.data['product_id'] is None:
            return Response(False, status=status.HTTP_200_OK)

        # Cartテーブルには外部キーがあるので外部キーのmember_idとproduct_idの値をそれぞれのテーブルから取得
        member_queryset = Member.objects.filter(id=request.data['member_id'])
        product_queryset = Product.objects.filter(id=request.data['product_id'])

        # Cartテーブルに登録
        cart = Cart.objects.create(
            member_id=member_queryset.get().id,
            product_id=product_queryset.get().id,
            quantity=request.data['quantity'],
        )
        cart.save()
    
        return Response(True, status=status.HTTP_200_OK)
        