from django.shortcuts import render
from rest_framework import generics
from members.models import Member
from .serializers import MemberSerializer
from .serializers import MemberAuthSerializer
from rest_framework.response import Response
import logging
from rest_framework import status
from datetime import datetime
from rest_framework import authentication

# 会員登録クラス
class MemberCreateAPIView(generics.ListCreateAPIView):
    def post(self, request, format=None, *args, **kwargs):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
           
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ログインクラス
class MemberAuthentocateAPIView(generics.CreateAPIView):
    #permission_classes = (IsAuthenticated)
    logfile = r"/Users/Tatsuki/projects/django/book_shop_api/book_shop_api/development.log"
    logging.basicConfig(filename=logfile,level=logging.DEBUG)
    
    serializer_class = MemberAuthSerializer
    
    #return Response(data={'mail_address': "test@test.com"}, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        logging.info("ddd")
        username = request.META.get('HTTP_X_USERNAME')
        logging.info(username)
        # リクエストからメールアドレスとトークンとパスワードを取得
        mail_address = request.POST['mail_address']
        password = request.POST['mail_address']
        logging.info(request.POST['csrfmiddlewaretoken'])
        # メールアドレス を元に該当するデータを検索
        queryset = Member.objects.filter(mail_address =mail_address)
        return Response(status=status.HTTP_200_OK)

    # def post(self, request, format=None):
    #     logging.info(request)
    #     return Response(data={'mail_address': "test@test.com"}, status=status.HTTP_200_OK)
        