from customer.models import Customer, CustomerProfile
from django.core.management.base import BaseCommand
from django.db.utils import Error


class Command(BaseCommand):
    help = 'Create customers'

    def handle(self, *args, **kwargs):
        try:
            c1 = Customer.objects.create(username='bmw_customer', email='bmw_customer@test.com', password='123')
            p1 = CustomerProfile.objects.get(user=c1.pk)

            q1 = {
                "make": "BMW",
                "model": "",
                "engine": "",
                "year": "",
                "color": "",
                "price": "",
            }

            p1.balance = 100000
            p1.title = "BMW_CUSTOMER"
            p1.customer_query = q1
            p1.save()

            c2 = Customer.objects.create(username='audi_customer', email='audi_customer@test.com', password='123')
            p2 = CustomerProfile.objects.get(user=c2.pk)
            q2 = {
                "make": "AUDI",
                "model": "",
                "engine": "",
                "year": "",
                "color": "",
                "price": "",
            }
            p2.balance = 100000
            p2.title = "AUDI_CUSTOMER"
            p1.customer_query = q2
            p2.save()


        except Error:
            print('users exist')

# python manage.py create_customers
