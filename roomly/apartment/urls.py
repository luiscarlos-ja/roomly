from django.urls import path, include
from .views import apartamentoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'apartamentos', apartamentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


