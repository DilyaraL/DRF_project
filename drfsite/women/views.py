from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import WomenSerializer


class WomenAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size' # можно через параметр в Get-запросе указать другое page_size
    max_page_size = 10000 # но пользователь не может указать больше этого значения


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = WomenAPIListPagination


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,) # пользователи смогут заходить только по токенам


class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly,)

# class WomenViewSet(viewsets.ModelViewSet):
#     """"""
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#     def qet_queryset(self):
#         # Чтобы отображалось только первые 3 записи, queryset теперь можно не писать
#         pk = self.kwargs.get('pk')
#
#         if not pk:
#             return Women.objects.all()[:3]
#         # используем filter тк он тоже возвращает СПИСОК
#         return Women.objects.filter(pk=pk)
#
#     @action(methods=['get'], detail=True)  # False - возвращается список, True - одна запись
#     def category(self, request, pk=None):
#         # Будем выводить категории
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats': cats.name})