from django.urls import path

from .views import BookingsCreateListMyBooksAPIViewSet, BookingsRetrieveUpdateDestroyMyBooksAPIView

urlpatterns = [
    path('', BookingsCreateListMyBooksAPIViewSet.as_view(), name='new_booking'),
    path('<int:pk>/', BookingsRetrieveUpdateDestroyMyBooksAPIView.as_view(), name='new_booking'),
]
