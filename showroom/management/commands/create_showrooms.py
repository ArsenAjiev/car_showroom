from showroom.models import Showroom, ShowroomProfile
from django.core.management.base import BaseCommand
from django.db.utils import Error


class Command(BaseCommand):
    help = 'Create customers'

    def handle(self, *args, **kwargs):
        try:
            c1 = Showroom.objects.create(username='bmw_showroom', email='bmw_showroom@test.com', password='123')
            p1 = ShowroomProfile.objects.get(user=c1.pk)
            q1 = {
                "make": "BMW",
                "model": "",
                "engine": "",
                "year": "",
                "color": "",
                "price": "",
            }
            p1.balance = 100000
            p1.name = "BMW_SHOWROOM"
            p1.showroom_query = q1
            p1.save()

            c2 = Showroom.objects.create(username='audi_showroom', email='audi_showroom@test.com', password='123')
            p2 = ShowroomProfile.objects.get(user=c2.pk)
            q2 = {
                "make": "AUDI",
                "model": "",
                "engine": "",
                "year": "",
                "color": "",
                "price": "",
            }
            p2.balance = 100000
            p2.name = "AUDI_SHOWROOM"
            p2.showroom_query = q2
            p2.save()



        except Error:
            print('users exist')

# python manage.py create_showrooms
