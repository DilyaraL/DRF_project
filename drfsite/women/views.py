from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializers import WomenSerializer


class WomenAPIView(APIView):
    # queryset = Women.objects.all()# будем выводить все данные из таблицы Women
    # serializer_class = WomenSerializer

    def get(self, request):
        w = Women.objects.all()
        return Response({'posts': WomenSerializer(w, many=True).data}) #передаем список статей, поэтому many=True

    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True) #raise_exception чтобы клиенту была понятна ошибка

        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )

        return Response({'post': WomenSerializer(post_new).data})
