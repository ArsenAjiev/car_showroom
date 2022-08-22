from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# car instance
class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    engine = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[MinValueValidator(0.6), MaxValueValidator(9.9)],
    )
    year = models.IntegerField(
        validators=[MinValueValidator(1980), MaxValueValidator(2021)]
    )
    color = models.CharField(max_length=10)
    price = models.DecimalField(
        max_digits=8, decimal_places=2, validators=[MinValueValidator(0.00)]
    )

    def __str__(self):
        return self.make
