from rest_framework import serializers
from .models import Actions
# pylint: disable=too-few-public-methods

class ActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actions
        fields = '__all__'

