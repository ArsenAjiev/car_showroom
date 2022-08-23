from car.models import Car
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create cars'

    def handle(self, *args, **kwargs):
        Car.objects.create(make='BMW', model='X5', engine=3.0, year=2000, color='red', is_active=True)
        Car.objects.create(make='BMW', model='X3', engine=3.0, year=2001, color='blue', is_active=True)
        Car.objects.create(make='BMW', model='X6', engine=3.0, year=2000, color='red', is_active=True)
        Car.objects.create(make='BMW', model='X7', engine=3.0, year=2000, color='green', is_active=False)

        Car.objects.create(make='AUDI', model='Q3', engine=3.0, year=2000, color='red', is_active=True)
        Car.objects.create(make='AUDI', model='Q4', engine=3.0, year=2000, color='blue', is_active=True)
        Car.objects.create(make='AUDI', model='Q5', engine=3.0, year=2000, color='red', is_active=True)
        Car.objects.create(make='AUDI', model='Q7', engine=3.0, year=2000, color='green', is_active=False)


# python manage.py create_cars

