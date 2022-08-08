from django.db import models
from core.abs_manager import DealerManager

from django.db.models.signals import post_save
from django.core.validators import MinValueValidator, MaxValueValidator
from django.dispatch import receiver
from core.models import User

# DEALER MODELS


class Dealer(User):
    base_role = User.Role.DEALER
    dealer_obj = DealerManager()

    class Meta:
        proxy = True

    def __str__(self):
        return f"{self.username} - {self.role}"


class DealerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=10, blank=True, null=True)
    date_created = models.IntegerField(
        default=1990, validators=[MinValueValidator(1990), MaxValueValidator(2022)]
    )
    description = models.TextField(blank=True, null=True)
    cars = models.ManyToManyField("car.Car", through="DealerCar")

    def __str__(self):
        return f"{self.user} - {self.name}"


@receiver(post_save, sender=Dealer)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "DEALER":
        DealerProfile.objects.create(user=instance)


class DealerCar(models.Model):
    car = models.ForeignKey("car.Car", on_delete=models.CASCADE)
    dealer = models.ForeignKey(DealerProfile, on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=8, decimal_places=2, validators=[MinValueValidator(0.00)], default=0.00
    )
    count = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.car.make} - {self.dealer.user.username}"
