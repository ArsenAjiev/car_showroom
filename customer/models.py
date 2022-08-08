from django.db import models
from core.abs_manager import CustomerManager

from django.db.models.signals import post_save
from django.core.validators import MinValueValidator
from django.dispatch import receiver
from core.models import User


# -----CUSTOMER MODELS---------------

# class Customer
class Customer(User):
    base_role = User.Role.CUSTOMER
    customer_obj = CustomerManager()

    class Meta:
        # proxy means that Customer and User have the same table in db
        proxy = True
        ordering = ["pk"]

    def __str__(self):
        return f"{self.username} - {self.role}"


# CustomerProfile created automatically when creating a Customer
class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    balance = models.DecimalField(
        max_digits=8, decimal_places=2, validators=[MinValueValidator(0.00)], default=0
    )
    cars = models.ManyToManyField("showroom.ShowroomCar", through="CustomerCar")

    def __str__(self):
        return f"{self.user.username}"


# signal create CustomerProfile created automatically when creating a Customer
@receiver(post_save, sender=Customer)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "CUSTOMER":
        CustomerProfile.objects.create(user=instance)


# cars bought by the user
class CustomerCar(models.Model):
    car = models.ForeignKey("showroom.ShowroomCar", on_delete=models.CASCADE)
    customer = models.ForeignKey("customer.CustomerProfile", on_delete=models.CASCADE)
    showroom = models.ForeignKey("showroom.ShowroomProfile", on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    price = models.DecimalField(
        max_digits=8, decimal_places=2, validators=[MinValueValidator(0.00)], default=0.00
    )

    def __str__(self):
        return f"{self.car.car.car.make} - {self.customer.user.username}"
