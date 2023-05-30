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

    def create(self, validated_data):
        return Women.objects.create(**validated_data) #добавляем новую запись в таблицу

    def update(self, instance, validated_data): #instance - ссылка на объект модели
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        instance.save()
        return instance
