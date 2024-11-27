from django.db import models
from uuid import uuid4
from datetime import datetime

class HotelAmenity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE, related_name='amenities')
    amenity = models.ForeignKey('Amenity', on_delete=models.CASCADE, related_name='hotels')
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            "id": str(self.id),
            "hotel": self.hotel.to_dict() if self.hotel else None,
            "amenity": self.amenity.to_dict() if self.amenity else None,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def __str__(self):
        return f"{self.hotel} - {self.amenity}"
