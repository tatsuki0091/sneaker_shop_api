from django.shortcuts import render
from rest_framework import generics
from members.models import Member
from .serializers import MemberSerializer
from rest_framework.response import Response
import logging
from rest_framework import status
from datetime import datetime

class MemberCreateAPIView(generics.ListCreateAPIView):
    logfile = r"/Users/Tatsuki/projects/django/book_shop_api/book_shop_api/development.log"
    logging.basicConfig(filename=logfile,level=logging.DEBUG)
    logging.info("post前")
    def post(self, request, format=None, *args, **kwargs):
        serializer = MemberSerializer(data=request.data)
        logging.info("post後")
        if serializer.is_valid(raise_exception=True):
            serializer.save()
           
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        