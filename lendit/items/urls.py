from django.urls import path,include
from .views import ItemListAPIViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register('', ItemListAPIViewSet, basename='items')

urlpatterns = [
    path('', include( router.urls)),
]