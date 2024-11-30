from django.db import models
from uuid import uuid4
from django.utils import timezone

class Amenity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False) 
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    hotel_amenities = models.ManyToManyField('Hotel', through='HotelAmenity')

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            "id": str(self.id),
            "name": self.name,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def __str__(self):
        return self.name
