from django.db import models
from uuid import uuid4
from django.utils import timezone

class Discount(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    code = models.CharField(max_length=100)
    discount = models.FloatField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=20, default='Active', choices=[('Active', 'Active'), ('Inactive', 'Inactive')]) #! Active/Inactive
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            "id": str(self.id),
            "code": self.code,
            "discount": self.discount,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def __str__(self):
        return self.code + " " + str(self.discount) + " " + str(self.start_date) + " " + str(self.end_date) + " " + self.status
