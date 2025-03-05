from rest_framework import serializers
from .models import apartamento

class apartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = apartamento
        fields = ['id', 'name', 'rooms', 'bathrooms', 'price', 'description', 'created_at', 'updated_at', 'is_available', 'camas']