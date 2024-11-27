from django.db import models
from uuid import uuid4
from datetime import datetime

class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    zip_code = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            "country": self.country,
            "city": self.city,
            "address": self.address,
            "zip_code": self.zip_code,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def __str__(self):
        return self.country + " " + self.city + " " + self.address + " " + str(self.zip_code)
