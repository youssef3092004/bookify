from django.db import models
from uuid import uuid4
from django.utils import timezone

class DiscountUserHotel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    discount = models.ForeignKey('Discount', on_delete=models.CASCADE, related_name='discount_user_hotels')
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='discount_user_hotels')
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE, related_name='discount_user_hotels')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            "id": str(self.id),
            "discount": self.discount.to_dict() if self.discount else None,
            "user": self.user.to_dict() if self.user else None,
            "hotel": self.hotel.to_dict() if self.hotel else None,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def __str__(self):
        return f"Discount {self.discount.discount}% for {self.user.username} at {self.hotel.name}"
