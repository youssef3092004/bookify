from django.db import models
from uuid import uuid4
from django.utils import timezone

class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    total_price = models.FloatField()
    status = models.CharField(max_length=20, default='Pending', choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')]) #! Pending / Confirmed / Cancelled
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey ('User', on_delete=models.CASCADE, related_name='booking')
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE, related_name='booking')
    room = models.ForeignKey('Room', on_delete=models.CASCADE, related_name='booking')

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            "id": str(self.id),
            "check_in": self.check_in,
            "check_out": self.check_out,
            "total_price": self.total_price,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "user": self.user.to_dict() if self.user else None,
            "hotel": self.hotel.to_dict() if self.hotel else None,
            "room": self.room.to_dict() if self.room else None,
        }

    def __str__(self):
        return f"Booking for {self.user.username} in room {self.room.room_number} from {self.check_in} to {self.check_out}"
