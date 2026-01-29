from rest_framework import serializers

from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    price_per_day = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    final_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    class Meta:
        model = Booking
        fields = ('item','customer','start_data','end_data','price_per_day','final_price','status')
        read_only_fields = ('customer','status',)


    def create(self, validated_data):
        validated_data['customer'] = self.context['request'].user
        item = validated_data['item']
        total_days = (validated_data['end_data'] - validated_data['start_data']).days
        validated_data['price_per_day'] = item.price
        validated_data['final_price'] = item.price * total_days
        print('----->', validated_data)
        return Booking.objects.create(**validated_data)