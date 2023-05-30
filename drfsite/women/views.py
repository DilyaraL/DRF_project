from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializers import WomenSerializer


class WomenViewSet(viewsets.ModelViewSet):
    """"""
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


# class WomenAPIList(generics.ListCreateAPIView):
#     """Будет возвращать и список записей по get-запросы и
#     добавлять запись по post-запросу"""
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenAPIUpdate(generics.UpdateAPIView):
#     """Будем возвращать измененную запись для запросов put и patch"""
#     queryset = Women.objects.all() # на самом деле тут будут отправляться не все записи, а только измененная, тк запрос ленивый
#     serializer_class = WomenSerializer
#
#
# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     """чтение, изменение и добавление отдельной записи (GET-, PUT-, PATCH- и DELETE-запросы)"""
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

