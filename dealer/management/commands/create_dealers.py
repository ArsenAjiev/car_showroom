from dealer.models import Dealer, DealerProfile
from django.core.management.base import BaseCommand
from django.db.utils import Error


class Command(BaseCommand):
    help = 'Create customers'

    def handle(self, *args, **kwargs):
        try:
            c1 = Dealer.objects.create(username='bmw_dealer', email='bmw_dealer@test.com', password='123')
            p1 = DealerProfile.objects.get(user=c1.pk)

            p1.title = "BMW_DEALER"
            p1.date_created = 2000
            p1.description = 'description'
            p1.balance = 100000
            p1.save()


            c2 = Dealer.objects.create(username='audi_dealer', email='audi_dealer@test.com', password='123')
            p2 = DealerProfile.objects.get(user=c2.pk)

            p2.title = "AUDI_DEALER"
            p2.date_created = 2000
            p2.description = 'description'
            p2.balance = 100000
            p2.save()



        except Error:
            print('users exist')

# python manage.py create_showrooms
