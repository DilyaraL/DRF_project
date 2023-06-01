from rest_framework import serializers

from .models import Women


class WomenSerializer(serializers.ModelSerializer):  # Сериализатор, кот. работает с Моделями
    # будем брать из таблицы определенные записи, представлять их в json
    # и отправлять в ответ на запрос пользователю
    # атрибут пользователь = в скрытом поле по умолчанию прописывается тек. пользователь
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Women
        # fields = ('title', 'content', 'cat')  # поля, кот. будут отправляться. записываются как в модели
        fields = "__all__" #- если хотим, чтобы все поля вывелись
