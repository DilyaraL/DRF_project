from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import WomenSerializer


class WomenViewSet(viewsets.ModelViewSet):
    """"""
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

    def qet_queryset(self):
        # Чтобы отображалось только первые 3 записи, queryset теперь можно не писать
        pk = self.kwargs.get('pk')

        if not pk:
            return Women.objects.all()[:3]
        # используем filter тк он тоже возвращает СПИСОК
        return Women.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)  # False - возвращается список, True - одна запись
    def category(self, request, pk=None):
        # Будем выводить категории
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})

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
