from django.db import models
from uuid import uuid4
from django.utils import timezone
from django.apps import apps  # For dynamic importing

class HotelAmenity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE)
    amenity = models.ForeignKey('Amenity', on_delete=models.CASCADE)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        hotel_model = apps.get_model('main', 'Hotel')
        amenity_model = apps.get_model('main', 'Amenity')
        return {
            "id": str(self.id),
            "hotel": hotel_model.objects.get(id=self.hotel.id).to_dict() if self.hotel else None,
            "amenity": amenity_model.objects.get(id=self.amenity.id).to_dict() if self.amenity else None,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def __str__(self):
        return f"Hotel: {self.hotel.name}, Amenity: {self.amenity.name}, Room: {self.room.name}"
