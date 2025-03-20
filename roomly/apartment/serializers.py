from rest_framework import serializers
from .models import apartamento

class apartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = apartamento
        fields = '__all__'