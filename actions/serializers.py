"""
Serializer for translating our models to JSON
"""
from rest_framework import serializers
from .models import Actions

class ActionsSerializer(serializers.ModelSerializer):
    """ Serializer for Actions """
    class Meta:
        """ specify which model/fields the serializer represents """
        model = Actions
        fields = '__all__'

# FUTURE ADD SUPPORT FOR MULTIPLE PROMPTS
#class PromptsSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Prompts
#        fields = '__all__'
