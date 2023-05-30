from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializers import WomenSerializer


class WomenAPIList(generics.ListCreateAPIView):
    """Будет возвращать и список записей по get-запросы и
    добавлять запись по post-запросу"""
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIUpdate(generics.UpdateAPIView):
    """Будем возвращать измененную запись для запросов put и patch"""
    queryset = Women.objects.all() # на самом деле тут будут отправляться не все записи, а только измененная, тк запрос ленивый
    serializer_class = WomenSerializer


class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    """чтение, изменение и добавление отдельной записи (GET-, PUT-, PATCH- и DELETE-запросы)"""
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

# class WomenAPIView(APIView):
#     # queryset = Women.objects.all()# будем выводить все данные из таблицы Women
#     # serializer_class = WomenSerializer
#
#     def get(self, request):
#         w = Women.objects.all()
#         return Response({'posts': WomenSerializer(w, many=True).data})  # передаем список статей, поэтому many=True
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)  # raise_exception чтобы клиенту была понятна ошибка
#         serializer.save()  # автоматически вызовет метод create
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({'error': 'Method PUT not allowed'})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object does not exists'})
#
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()  # вызовет метод update, тк при создании Сериализатора было указано ДВА параметра: data, instance
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({'error': 'Method DELETE not allowed'})
#
#         try:
#             Women.objects.get(pk=pk).delete()
#         except:
#             return Response({'error': 'Object does not exists'})
#
#         return Response({"post": "delete post " + str(pk)})
