from django.db import models
from django.contrib.auth.models import AbstractUser


# base class for all models
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        CUSTOMER = "CUSTOMER", "Customer"
        DEALER = "DEALER", "Dealer"
        SHOWROOM = "SHOWROOM", "Showroom"

    base_role = Role.ADMIN
    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)
