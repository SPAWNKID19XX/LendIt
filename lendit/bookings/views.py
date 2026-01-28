from gc import get_objects

from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.db.models import Q

from .serializers import BookingSerializer
from .models import Booking, StatusBooking


# Create your views here.

class BookingsCreateListMyBooksAPIViewSet(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = Booking.objects.select_related('item','customer','item__owner')
        return qs.filter(Q(item__owner=self.request.user) | Q(customer=self.request.user))

class BookingsRetrieveUpdateDestroyMyBooksAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookingSerializer

    def perform_update(self, serializer):
        instance = self.get_object()
        new_status = serializer.validated_data.get('status', None)

        if instance.status in [StatusBooking.CANCELED, StatusBooking.REJECTED]:
            raise PermissionDenied(detail=f"Booking already {instance.status}. Update does not allowed")

        if new_status and new_status in [StatusBooking.CONFIRMED, StatusBooking.REJECTED]:
            if self.request.user != instance.item.owner:
                raise  PermissionDenied(detail=f"Booking could be Updated Just By owner")
        if new_status and new_status == StatusBooking.CANCELED:
            if self.request.user != instance.customer:
                raise PermissionDenied(detail=f"Booking could be Canceled Just By customer")
        if instance.status == StatusBooking.CONFIRMED:
            if 'start_date' in serializer.validated_data or 'end_date' in serializer.validated_data:
                if instance.start_data != serializer.validated_data['start_date'] or instance.end_data != serializer.validated_data['end_date']:
                    raise PermissionDenied("Dates are frozen once confirmed.")
        serializer.save()
