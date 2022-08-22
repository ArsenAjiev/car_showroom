from django.db import models
from django_countries.fields import CountryField
from django.db import models
from core.abs_manager import ShowroomManager

from django.db.models.signals import post_save
from django.core.validators import MinValueValidator
from django.dispatch import receiver
from core.models import User


class Showroom(User):
    base_role = User.Role.SHOWROOM
    showroom_obj = ShowroomManager()

    class Meta:
        proxy = True

    def __str__(self):
        return f"{self.username} - {self.role}"


class ShowroomProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    location = CountryField(blank=True, null=True)
    # query to the dealer another name11
    car_description = models.JSONField(
        default=dict({
            "make": "",
            "model": "",
            "color": "",
            "year": "",
            "engine": "",
            "price": "",
        })
    )
    balance = models.DecimalField(
        max_digits=8, decimal_places=2, validators=[MinValueValidator(0.00)], default=0
    )
    cars = models.ManyToManyField("dealer.DealerCar", through="ShowroomCar")

    def __str__(self):
        return f"{self.user} - {self.name}"


# signal create ShowroomProfile created automatically when Showroom creating
@receiver(post_save, sender=Showroom)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "SHOWROOM":
        ShowroomProfile.objects.create(user=instance)


class ShowroomCar(models.Model):
    car = models.ForeignKey("dealer.DealerCar", on_delete=models.CASCADE)
    showroom = models.ForeignKey(ShowroomProfile, on_delete=models.CASCADE)
    dealer = models.ForeignKey("dealer.DealerProfile", on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=8, decimal_places=2, validators=[MinValueValidator(0.00)], default=0
    )
    count = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.car.car.make} - {self.showroom.user.username}"
