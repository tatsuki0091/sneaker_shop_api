from django.shortcuts import render
from rest_framework import generics
from members.models import Member
from .serializers import MemberSerializer
from .serializers import MemberAuthSerializer
from .serializers import GetMemberInfoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import logging
from rest_framework import status
from datetime import datetime
from rest_framework import authentication
import hashlib
# パスワードハッシュ化のためのライブラリ
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

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
    
    serializer_class = MemberAuthSerializer
    
    #return Response(data={'mail_address': "test@test.com"}, status=status.HTTP_200_OK)
    def post(self, request, format=None):

        mail_address = request.data['mail_address']
        password = request.data['password']

        # メールアドレス を元に該当するデータを検索
        queryset = Member.objects.filter(mail_address=mail_address)

        # データ存在判定
        if len(queryset) ==0:
            # エラー時のメッセージを設定
            message = "メールアドレス 、またはパスワードに誤りがあります。"
            return Response(message, status=status.HTTP_200_OK)
        else:
            #  パスワード一致判定
            if check_password(password, queryset.get().password):
                # ユーザIDをハッシュ化してsessionに格納1
                # request.session['user_id'] = hashlib.md5(str(queryset.get().id).encode("utf-8")).hexdigest()
                request.session['user_id'] = str(queryset.get().id )
                return Response(request.session['user_id'], status=status.HTTP_200_OK)
        
        return Response(message, status=status.HTTP_200_OK)
        
# 会員情報取得
class GetMemberInfoAPIView(generics.RetrieveDestroyAPIView):
    def post(self, request, format=None, *args, **kwargs):
        # リクエストの値のNULL、空白判定
        if not request.data['user_id']:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            # 主キーでデータを検索
            queryset = Member.objects.get(pk=request.data['user_id'])
            serializer_class = GetMemberInfoSerializer
            # シリアライザにデータを設定
            serializer = serializer_class(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)

# 会員情報更新
class UpdateMemberInfoAPIView(generics.UpdateAPIView):
    def post(self, request, format=None, *args, **kwargs):
        logfile = r"/Users/Tatsuki/projects/django/book_shop_api/book_shop_api/development.log"
        logging.basicConfig(filename=logfile, level=logging.DEBUG)

        logging.info(request.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        # # リクエストの値のNULL、空白判定
        # if not request.data['user_id']:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     # 主キーでデータを検索
        #     queryset = Member.objects.get(pk=request.data['user_id'])
        #     serializer_class = GetMemberInfoSerializer
        #     # シリアライザにデータを設定
        #     serializer = serializer_class(queryset)
        #     return Response(serializer.data, status=status.HTTP_200_OK)

