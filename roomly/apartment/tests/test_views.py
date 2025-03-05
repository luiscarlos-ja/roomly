from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apartment.models import apartamento
from decimal import Decimal

class ApartamentoViewSetTest(APITestCase):
    def setUp(self):
        self.apartment = apartamento.objects.create(
            name="Test Apartment",
            rooms=2,
            bathrooms=1,
            price=Decimal('1000.00'),
            description="Test description",
            camas=3,
            is_available=True
        )
        self.list_url = reverse('apartamento-list')
        self.detail_url = reverse('apartamento-detail', args=[self.apartment.id])

    def test_list_apartments(self):
        """Test retrieving a list of apartments"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_apartment(self):
        """Test creating a new apartment"""
        data = {
            'name': 'New Apartment',
            'rooms': 3,
            'bathrooms': 2,
            'price': '1500.00',
            'description': 'New description',
            'camas': 4,
            'is_available': True
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(apartamento.objects.count(), 2) 