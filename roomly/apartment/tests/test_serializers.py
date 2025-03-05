from django.test import TestCase
from apartment.models import apartamento
from apartment.serializers import apartamentoSerializer
from decimal import Decimal

class ApartamentoSerializerTest(TestCase):
    def setUp(self):
        self.apartment_data = {
            'name': 'Test Apartment',
            'rooms': 2,
            'bathrooms': 1,
            'price': '1000.00',
            'description': 'Test description',
            'camas': 3,
            'is_available': True
        }
        self.apartment = apartamento.objects.create(**self.apartment_data)
        self.serializer = apartamentoSerializer(instance=self.apartment)

    def test_contains_expected_fields(self):
        """Test that serializer contains all expected fields"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'name', 'rooms', 'bathrooms', 
                                              'price', 'description', 'created_at', 
                                              'updated_at', 'is_available', 'camas']))

    def test_field_content(self):
        """Test that serializer data matches model instance"""
        data = self.serializer.data
        self.assertEqual(data['name'], self.apartment_data['name'])
        self.assertEqual(data['rooms'], self.apartment_data['rooms'])
        self.assertEqual(data['bathrooms'], self.apartment_data['bathrooms'])
        self.assertEqual(data['description'], self.apartment_data['description'])
        self.assertEqual(data['camas'], self.apartment_data['camas'])
        self.assertEqual(data['is_available'], self.apartment_data['is_available']) 