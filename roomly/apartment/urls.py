from django.urls import path, include
from .views import apartamentoView
#from .views import apartamentoViewSet
#from rest_framework.routers import DefaultRouter

#router = DefaultRouter()
# router.register(r'apartamentos', apartamentoViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]
urlpatterns = [
     path('', apartamentoView.as_view(), name= 'apartment_List'),
     path('<int:id>', apartamentoView.as_view(), name= 'apartment_Detail'),
 ]


