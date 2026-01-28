from django.db import models
from django.core.exceptions import ValidationError
from users.models import CustomUser
from items.models import Item
from django.conf import settings
from datetime import timedelta
# Create your models here.

class StatusBooking(models.TextChoices):
    PENDING = "PENDING", "PENDING"
    CONFIRMED = "CONFIRMED", "CONFIRMED"
    REJECTED = "CANCELED", "CANCELED"


class Booking(models.Model):
    item = models.ForeignKey(Item   , on_delete=models.CASCADE)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    final_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(choices=StatusBooking.choices, default=StatusBooking.PENDING, max_length=10)

    def __str__(self):
        return f"{self.item} - {self.item.owner} - {self.start_date} - {self.end_date}"

    def save(self, *args, **kwargs):
        if self.end_date < self.start_date:
            raise ValidationError("Start date must be before end date")
        qs = Booking.objects.filter(item=self.item, start_date__lte=self.end_date,
                                    end_date__gte=self.start_date).exclude(status=StatusBooking.REJECTED).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError("Item is busy")
        if not self.id:
            days = max((self.end_date - self.start_date).days, 1)
            print("not exist: - ", days)
            self.price_per_day = self.item.price
            self.final_price = self.price_per_day * days

        super(Booking, self).save(*args, **kwargs)