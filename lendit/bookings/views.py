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
        old_status = instance.status
        item = serializer.validated_data.get('item', self.get_object().item)
        owner = item.owner
        if self.request.user != owner:
            raise PermissionDenied('You are not allowed to perform this action')
        if old_status == StatusBooking.CONFIRMED:
            if 'start_date' in serializer.validated_data or 'end_date' in serializer.validated_data:
                raise PermissionDenied("You cannot change dates of a confirmed booking.")

        new_status = serializer.validated_data.get('status')

        if new_status:
            if new_status in [Booking.CONFIRMED, Booking.PENDING]:
                raise PermissionDenied("Only owner could confirm/reject the booking.")
            if new_status == Booking.CANCELED:
                raise PermissionDenied("Only renter can cancel booking.")

        serializer.save()
