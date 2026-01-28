from rest_framework import serializers

from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    price_per_day = serializers.DecimalField(max_digits=10, decimal_places=2)
    final_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        model = Booking
        fields = ('item','customer','start_date','end_date','price_per_day','final_price','status')
        read_only_fields = ('customer','price_per_day','final_price','status',)


    def create(self, validated_data):
        validated_data['customer'] = self.context['request'].user
        return Booking.objects.create(**validated_data)