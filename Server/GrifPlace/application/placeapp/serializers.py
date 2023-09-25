from rest_framework import serializers
from .models import Access,Flat
"""
    В данном модуле реализуются сериализаторы DRF, позволяющие 
    валидировать данные для моделей DAO (models.py), 
    а также сериализующие (преобразующие) эти модели в стандартные 
    объекты Python (dict) и в формат json. Подробнее см.: 
    https://www.django-rest-framework.org/api-guide/serializers/
    https://www.django-rest-framework.org/api-guide/fields/
    
    Сериализаторы DRF являются аналогом DTO для Django. 
"""


class PeopleSerializer(serializers.Serializer):
    passport_number = serializers.IntegerField()
    first_name = serializers.CharField()  # объявление необязательного поля (may be None)
    second_name = serializers.CharField()
    phone_number = serializers.IntegerField()
    password = serializers.CharField()

    """ Класс Serializer позволяет переопределить наследуемые 
        методы create() и update(), в которых, например, можно реализовать бизнес-логику 
        для сохранения или обновления валидируемого объекта (например, для DAO ) """

class FlatSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    type = serializers.CharField()
    area = serializers.IntegerField()
    password = serializers.CharField()
    humidity = serializers.FloatField()
    temperature = serializers.FloatField()


class AccessSerializer1(serializers.Serializer):
    id = serializers.IntegerField()
    passport_number = serializers.RelatedField(source='people',read_only='True')
    flat_id = serializers.RelatedField(source='flat', read_only='True')
    date = serializers.DateTimeField()
    condition = serializers.CharField()
    reason = serializers.CharField()

class AccessSerializer2(serializers.Serializer):
    id = serializers.IntegerField()
    passport_number = PeopleSerializer()
    flat_id = FlatSerializer()
    date = serializers.DateTimeField()
    condition = serializers.CharField()
    reason = serializers.CharField()


class AccessSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    passport_number = serializers.IntegerField()
    flat_id = serializers.IntegerField()
    date = serializers.DateTimeField()
    condition = serializers.CharField()
    reason = serializers.CharField()
    

