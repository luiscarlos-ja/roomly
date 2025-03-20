from django.shortcuts import render
from .models import apartamento
from rest_framework import viewsets
from .serializers import apartamentoSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .services import apartmentService
from rest_framework.exceptions import ValidationError
import json
class apartamentoView(APIView):
    def get(self, request, id = None):
        if id is not None:
            apartament = apartmentService.find_apartment(id)
            if apartament:
                return Response(apartamentoSerializer(apartament).data)
            return Response({ "mensaje": "Error, apartamento no encontrado"}, status= status.HTTP_404_NOT_FOUND)
        aparments = apartmentService.list_apartments()
        if aparments:
            return Response(apartamentoSerializer(aparments, many = True).data)
        return Response({ "mensaje": "Error, No hay apartamentos"}, status= status.HTTP_404_NOT_FOUND)
    # def get_detail(self, request, id):
    #     apartament = apartmentService.find_apartment(id)
    #     if apartament:
    #         return Response(apartamentoSerializer(apartament).data)
    #     return Response({ "mensaje": "Error, apartamento no encontrado"}, status= status.HTTP_404_NOT_FOUND)
    def post(self, request):
        try:
            serializer = apartamentoSerializer(data = request.data)
            if serializer.is_valid(raise_exception=True):
                apartment = apartmentService.create_apartment(serializer.validated_data)
                serializer = apartamentoSerializer(apartment)
                return Response({"Message": "creation succesfull","apartment": json.dumps(serializer.data)})
            return Response ({"Message": "error al crear"})
        except ValidationError as e:
            return Response({"error": e.detail}, status=status.HTTP_400_BAD_REQUEST)
    
    # def delete(self,request,id = None):
    #     try:
    #         apartament = apartmentService.delete_apartment(id = id)

