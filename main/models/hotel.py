from django.db import models
from uuid import uuid4
from datetime import datetime

class Hotel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    property_type = models.CharField(max_length=50, null=False)  #! Hotel, Villa, etc.
    star_rating = models.IntegerField(null=False)  #! Star rating (1-5)
    num_rooms = models.IntegerField(null=False)
    contact_info = models.CharField(max_length=255, null=True, blank=True)
    images = models.JSONField(null=True, blank=True)  
    created_at = models.DateTimeField(default=datetime.now, editable=False)
    updated_at = models.DateTimeField(default=datetime.now)

#! relationships
    location = models.ForeignKey('Location', on_delete=models.CASCADE, related_name='hotels')
    rooms = models.ForeignKey('Room', on_delete=models.CASCADE, related_name='hotels')
    amenities = models.ManyToManyField('Amenity', related_name='hotels')
    reviews = models.ManyToManyField('Review', related_name='hotels')

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            "id": str(self.id),
            "name": self.name,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "property_type": self.property_type,
            "star_rating": self.star_rating,
            "num_rooms": self.num_rooms,
            "contact_info": self.contact_info,
            "images": self.images,
            "location": self.location.to_dict() if self.location else None,
            "rooms": [room.to_dict() for room in self.rooms.all()],
            "amenities": [amenity.to_dict() for amenity in self.amenities.all()],
            "reviews": [review.to_dict() for review in self.reviews.all()],
        }
    def __str__(self):
        return f"{self.name} ({self.property_type})"
