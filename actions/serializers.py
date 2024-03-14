from rest_framework import serializers
from .models import Actions, Context
# pylint: disable=too-few-public-methods

class ActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actions
        fields = '__all__'

class ContextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Context
        fields = '__all__'
