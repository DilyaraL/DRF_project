from rest_framework import serializers

from .models import Women


class WomenSerializer(serializers.Serializer): #Сериализатор, кот. работает с Моделями
    # будем брать из таблицы определенные записи, представлять их в json
    # и отправлять в ответ на запрос пользователю
    # class Meta:
    #     model = Women
    #     fields = ('title', 'cat_id') #поля, кот. будут отправляться
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()
