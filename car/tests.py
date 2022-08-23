from django.test import TestCase
from car.models import Car


class TestCategoryModel(TestCase):

    def test_create_car(self):
        """
        add car instance in Car model
        """
        car_1 = Car.objects.create(make='BMW', model='X5',engine=0.8, year=2000, color='red')
        self.assertEqual(car_1.make, 'BMW')



