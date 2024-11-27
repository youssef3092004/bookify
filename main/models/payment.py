""" Model definition for Payment. """
from django.db import models
from uuid import uuid4
from datetime import datetime


class Payment(models.Model):
    """Model definition for Payment."""
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    payment_method = models.CharField(
        max_length=50, 
        default='Credit Card', 
        choices=[('Credit Card', 'Credit Card'), 
                 ('Debit Card', 'Debit Card'), 
                 ('PayPal', 'PayPal')])
    status = models.CharField(max_length=50,
                                 default='Pending',
                                 choices=[('Pending', 'Pending'),
                                          ('Paid', 'Paid'),
                                          ('Failed', 'Failed')])
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='payment')
    booking = models.ForeignKey('Booking', on_delete=models.CASCADE, related_name='payment')

    @property
    def total_price(self):
        """Retrieve the total price from the related booking."""
        return self.booking.total_price if self.booking else None

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            "id": str(self.id),
            "payment_method": self.payment_method,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "user": self.user.to_dict() if self.user else None,
            "booking": self.booking.to_dict() if self.booking else None,
            "total_price": self.total_price,
        }

    def __str__(self):
        return f"{self.user.username} - {self.payment_method} - {self.status}"
