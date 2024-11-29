from django.db import models
from uuid import uuid4
from datetime import datetime

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.CharField(max_length=100, unique=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            "id": str(self.id),
            "username": self.username,
            "fname": self.fname,
            "lname": self.lname,
            "address": self.address,
            "phone": self.phone,
            "email": self.email,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def __str__(self):
        return self.username
