from django.db import models

# Create your models here.
class apartamento(models.Model):
    name = models.CharField(max_length=200)
    rooms = models.IntegerField()
    bathrooms = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    #image = models.ImageField(upload_to='apartments/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)
    camas = models.IntegerField()

    def __str__(self):
        return self.name

