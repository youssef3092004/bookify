from django.db import models
from uuid import uuid4
from datetime import datetime

class review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    rating = models.IntegerField() #! Rating (1-5)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='reviews')

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            "id": str(self.id),
            "description": self.description,
            "rating": self.rating,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def __str__(self):
        return f'({self.rating}⭐) {self.description}'
