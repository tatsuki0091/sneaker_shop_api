from django.shortcuts import render
from rest_framework import generics
from members.models import Member
from .serializers import MemberSerializer
from .serializers import MemberAuthSerializer
from .serializers import GetMemberInfoAndUpdateSerializer
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

from django.contrib.sessions.backends.db import SessionStore

# 会員登録クラス
class MemberCreateAPIView(generics.ListCreateAPIView):
    def post(self, request, format=None, *args, **kwargs):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ログインクラス
class MemberAuthentocateAPIView(generics.CreateAPIView):
    logfile = r"/Users/Tatsuki/projects/django/book_shop_api/book_shop_api/development.log"
    logging.basicConfig(filename=logfile, level=logging.DEBUG)
    
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
            #message = "メールアドレス 、またはパスワードに誤りがあります。"
            return Response(False, status=status.HTTP_200_OK)
        else:
            #  パスワード一致判定
            if check_password(password, queryset.get().password):
                # ユーザIDをハッシュ化してsessionに格納1
                # request.session['user_id'] = hashlib.md5(str(queryset.get().id).encode("utf-8")).hexdigest()
                # request.session['user_id'] = str(queryset.get().id )
                # logfile = r"/Users/Tatsuki/projects/django/book_shop_api/book_shop_api/development.log"
                # logging.basicConfig(filename=logfile, level=logging.DEBUG)
                # logging.info(request.session.get('user_id'))
                return Response(queryset.get().id, status=status.HTTP_200_OK)
            
        
        return Response(False, status=status.HTTP_200_OK)
        
# 会員情報取得
class GetMemberInfoAPIView(generics.RetrieveDestroyAPIView):
    def post(self, request, format=None, *args, **kwargs):
        # リクエストの値のNULL、空白判定
        if not request.data['user_id']:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            # 主キーでデータを検索
            queryset = Member.objects.get(pk=request.data['user_id'])
            serializer_class = GetMemberInfoAndUpdateSerializer
            # シリアライザにデータを設定
            serializer = serializer_class(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)

# 会員情報更新
class UpdateMemberInfoAPIView(generics.UpdateAPIView):
    logfile = r"/Users/Tatsuki/projects/django/book_shop_api/book_shop_api/development.log"
    logging.basicConfig(filename=logfile, level=logging.DEBUG)
    serializer_class = GetMemberInfoAndUpdateSerializer
    
    def post(self, request, format=None, *args, **kwargs):
        # セッションが存在するかどうか確認
        if len(request.data['user_id']):
            serializer_class = GetMemberInfoAndUpdateSerializer(data=request.data)
            Member.objects.filter(id=request.data['user_id']).update(
                first_name=request.data['first_name'],
                last_name=request.data['last_name'],
                mail_address = request.data['mail_address'],
                prefecture = request.data['prefecture'],
                address1 = request.data['address1'],
                address2 = request.data['address2'],
                phone_number = request.data['phone_number']
                )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
         # 主キーでデータを検索
        # queryset = Member.objects.get(pk=request.session['user_id'])
        # logging.info(queryset)

        #result = serializer_class.update(id=request.session['user_id'])
        return Response(True, status=status.HTTP_200_OK)
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

