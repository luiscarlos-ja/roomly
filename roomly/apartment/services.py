from .repositories import apartmentsRepository

class apartmentService():
    def list_apartments():
        return apartmentsRepository.get_all()
    def find_apartment(id):
        try:
            return apartmentsRepository.get_by_id(id)
        except ValueError:
            return None
    def create_apartment(data):
         apartment = apartmentsRepository.create(data)
         return apartment
        