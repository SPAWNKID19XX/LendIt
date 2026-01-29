from celery import Celery, shared_task
import time
import logging

from .models import Booking

logger = logging.getLogger(__name__)

@shared_task
def send_bookong_notifications(booking_id):
    booking = Booking.objects.get(id=booking_id)
    logger.info(f'Logs for booking: -> {booking} started here!')
    time.sleep(5)
    logger.info(f'Logs for booking: -> {booking} ended here!')
    return f"Booking notification: -> {booking} here!"
