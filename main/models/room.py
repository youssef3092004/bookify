from django.db import models
from uuid import uuid4
from datetime import datetime

class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    room_type = models.CharField(max_length=20, default='Single') #! Single, Double, Triple, Suite, deluxe etc
    room_number = models.IntegerField()
    price = models.FloatField()
    status = models.CharField(max_length=20, default='Available') #! Available, Booked, Under Maintenance
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE, related_name='rooms')
    booking = models.ForeignKey('Booking', on_delete=models.CASCADE, related_name='rooms')

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            "id": str(self.id),
            "hotel": self.hotel.to_dict() if self.hotel else None,
            "room_type": self.room_type,
            "room_number": self.room_number,
            "prince": self.price,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    def __str__(self):
        return f"{self.hotel} - {self.room_type} - {self.room_number}"
