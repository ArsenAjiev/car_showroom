from django.db import models
from showroom.models import ShowroomProfile
from django.core.validators import MinValueValidator
from car.models import Car
from dealer.models import DealerProfile


class DealerSales(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    discount = models.DecimalField(
        max_digits=3, decimal_places=2, validators=[MinValueValidator(0.00)], default=0.01
    )
    start_date = models.DateField()
    end_date = models.DateField()
    dealer = models.ForeignKey(DealerProfile, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    is_active = models.BooleanField()

    def __str__(self):
        return f"{self.title} - {self.discount} -{self.car.model}- {self.dealer.user}"


class ShowroomSales(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    discount = models.DecimalField(
        max_digits=3, decimal_places=2, validators=[MinValueValidator(0.00)], default=0.01
    )
    start_date = models.DateField()
    end_date = models.DateField()
    showroom = models.ForeignKey(ShowroomProfile, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    is_active = models.BooleanField()

    def __str__(self):
        return f"{self.title} - {self.discount} -{self.car.model}- {self.showroom.name}"
