from django.shortcuts import render
from .models import apartamento
from rest_framework import viewsets
from .serializers import apartamentoSerializer

class apartamentoViewSet(viewsets.ModelViewSet):
    queryset = apartamento.objects.all()
    serializer_class = apartamentoSerializer

# Create your views here.
