from django.test import TestCase
from .models import apartamento
from decimal import Decimal

class ApartamentoModelTest(TestCase):
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

    def test_apartment_creation(self):
        """Test that an apartment can be created with the correct attributes"""
        self.assertEqual(self.apartment.name, "Test Apartment")
        self.assertEqual(self.apartment.rooms, 2)
        self.assertEqual(self.apartment.bathrooms, 1)
        self.assertEqual(self.apartment.price, Decimal('1000.00'))
        self.assertEqual(self.apartment.description, "Test description")
        self.assertEqual(self.apartment.camas, 3)
        self.assertTrue(self.apartment.is_available)

    def test_string_representation(self):
        """Test the string representation of the apartment"""
        self.assertEqual(str(self.apartment), "Test Apartment")
