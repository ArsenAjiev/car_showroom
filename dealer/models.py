from django.db import models
from core.abs_manager import DealerManager
from core.abs_model_data import CommonInfo

from django.db.models.signals import post_save
from django.core.validators import MinValueValidator, MaxValueValidator
from django.dispatch import receiver
from core.models import User


class Dealer(User):
    base_role = User.Role.DEALER
    dealer_obj = DealerManager()

    class Meta:
        proxy = True

    def __str__(self):
        return f"{self.username} - {self.role}"


class DealerProfile(CommonInfo):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.IntegerField(
        default=1990, validators=[MinValueValidator(1990), MaxValueValidator(2022)]
    )
    description = models.TextField(blank=True, null=True)
    cars = models.ManyToManyField("car.Car", through="DealerCar")
    balance = models.DecimalField(
        max_digits=8, decimal_places=2, validators=[MinValueValidator(0.00)], default=0
    )

    def __str__(self):
        return f"{self.user} - {self.title} - {self.balance}"


@receiver(post_save, sender=Dealer)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "DEALER":
        DealerProfile.objects.create(user=instance)


class DealerCar(CommonInfo):
    car = models.ForeignKey("car.Car", on_delete=models.CASCADE)
    dealer = models.ForeignKey(DealerProfile, on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.00)],
        default=0.00,
    )
    count = models.IntegerField(default=1)

    class Meta:
        # there cannot be the same combinations
        unique_together = ('car', 'dealer',)

    def __str__(self):
        return f"{self.car.make} - {self.car.model} -{self.car.color}- {self.dealer.user.username} - {self.count} - {self.price} - {self.is_active}"


class TransactionSellToShowroom(models.Model):
    car = models.ForeignKey("car.Car", on_delete=models.CASCADE)
    showroom = models.ForeignKey("showroom.ShowroomProfile", on_delete=models.CASCADE)
    dealer = models.ForeignKey(DealerProfile, on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], default=0
    )
    count = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.car.make} - {self.car.model} - showroom:{self.showroom.name}\
        , dealer: {self.dealer.title}- count:{self.count} -price: {self.price}"
