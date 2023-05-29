from django.shortcuts import render
from rest_framework import generics
from .models import Women
from .serializers import WomenSerializer


class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.all()# будем выводить все данные из таблицы Women
    serializer_class = WomenSerializer
