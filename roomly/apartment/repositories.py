
from .models import apartamento
class apartmentsRepository():
    def get_all():
        return apartamento.objects.all()
    
    def get_by_id(id):
        try:
            return apartamento.objects.get(id = id)#apartamento.objects.filter(id = id).first()
        except apartamento.DoesNotExist:
            raise ValueError(" No existe el Apartamento")
        
    def create(data):
        return apartamento.objects.create(**data)
     