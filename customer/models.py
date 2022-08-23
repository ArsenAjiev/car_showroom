from django.db import models
from core.abs_manager import CustomerManager
from core.abs_model_data import CommonInfo

from django.db.models.signals import post_save
from django.core.validators import MinValueValidator
from django.dispatch import receiver
from core.models import User


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
class CustomerProfile(CommonInfo):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    customer_query = models.JSONField(
        default=dict(
            {
                "make": "",
                "model": "",
                "engine": "",
                "year": "",
                "color": "",
                "price": "",
            }
        )
    )
    balance = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], default=0
    )
    cars = models.ManyToManyField("car.Car", through="CustomerCar")

    def __str__(self):
        return f"{self.user.username} - {self.title} - {self.balance}"


# signal create CustomerProfile created automatically when creating a Customer
@receiver(post_save, sender=Customer)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "CUSTOMER":
        CustomerProfile.objects.create(user=instance)


# cars bought by the user
class CustomerCar(CommonInfo):
    car = models.ForeignKey("car.Car", on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    showroom = models.ForeignKey("showroom.ShowroomProfile", on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.00)],
        default=0.00,
    )

    def __str__(self):
        return f"{self.car.make} - {self.car.model} -{self.car.color}- count:{self.count}\
        {self.price} - {self.is_active} - {self.showroom.name}- {self.customer.title}"
