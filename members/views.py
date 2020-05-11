from django.shortcuts import render
from rest_framework import generics
from members.models import Member
from .serializers import MemberSerializer
from rest_framework.response import Response
import logging

class MemberCreateAPIView(generics.ListCreateAPIView):

    def post(self, request, format=None, *args, **kwargs):
        #first_name = request.GET.post("first_name") 
        logging.debug('debug message')
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            result = serializer.save()
            serializer = MemberSerializer(result)
            return Response(serializer.data)
        