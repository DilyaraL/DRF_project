from rest_framework import serializers

from .models import Women


class WomenSerializer(serializers.ModelSerializer): #Сериализатор, кот. работает с Моделями
    # будем брать из таблицы определенные записи, представлять их в json
    # и отправлять в ответ на запрос пользователю
    class Meta:
        model = Women
        fields = ('title', 'cat_id') #поля, кот. будут отправляться