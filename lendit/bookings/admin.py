from django.contrib import admin

from .models import Booking


# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ('item', 'customer','price_per_day','final_price')
    filds = ('item', 'customer','price_per_day','final_price','status','start_data','end_data')

admin.site.register(Booking, BookingAdmin)