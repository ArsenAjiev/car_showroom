from django.db import models
from django_countries.fields import CountryField
from core.abs_model_data import CommonInfo
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


class ShowroomProfile(CommonInfo):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    location = CountryField(blank=True, null=True)
    showroom_query = models.JSONField(
        default=dict(
            {
                "make": "",
                "model": "",
                "engine": "",
                "year": "",
                "color": "",
                "price": 0.00,
            }
        )
    )
    balance = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], default=0
    )
    cars = models.ManyToManyField("car.Car", through="ShowroomCar")

    def __str__(self):
        return f"{self.user} - {self.name} - {self.balance}"


@receiver(post_save, sender=Showroom)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "SHOWROOM":
        ShowroomProfile.objects.create(user=instance)


class ShowroomCar(CommonInfo):
    car = models.ForeignKey("car.Car", on_delete=models.CASCADE)
    showroom = models.ForeignKey(ShowroomProfile, on_delete=models.CASCADE)
    dealer = models.ForeignKey("dealer.DealerProfile", on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], default=0
    )
    count = models.IntegerField(default=1)

    class Meta:
        # there cannot be the same combinations
        unique_together = ('car', 'dealer', 'showroom')

    def __str__(self):
        return f"{self.car.make} -{self.car.model} - {self.car.color} - {self.showroom.user.username} - count: {self.count}\
         price: {self.price}- {self.is_active}"


class TransactionSellToCustomer(models.Model):
    car = models.ForeignKey("car.Car", on_delete=models.CASCADE)
    customer = models.ForeignKey("customer.CustomerProfile", on_delete=models.CASCADE)
    showroom = models.ForeignKey('showroom.ShowroomProfile', on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], default=0
    )
    count = models.IntegerField(default=1)

    def __str__(self):
        return f"car: {self.car.make} - model: {self.car.model} - showroom:{self.showroom.user.username} - \
         count: {self.count} - price: {self.price}  - customer: {self.customer.title} "
