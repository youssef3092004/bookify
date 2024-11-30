from django.db import models
from uuid import uuid4
from django.utils import timezone

class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    room_type = models.CharField(max_length=20, default='Single', choices=[('Single', 'Single'), ('Double', 'Double'), ('Triple', 'Triple'), ('Suite', 'Suite'), ('deluxe', 'deluxe')])
    room_number = models.IntegerField()
    price = models.FloatField()
    status = models.CharField(
        max_length=20, 
        default='Available', 
        choices=[
            ('Available', 'Available'), 
            ('Booked', 'Booked'), 
            ('Under Maintenance', 'Under Maintenance')
        ]
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE, related_name='room_set')
    amenities = models.ManyToManyField('Amenity', through='HotelAmenity')
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
