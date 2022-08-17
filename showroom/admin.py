from django.contrib import admin
from showroom.models import Showroom, ShowroomProfile, ShowroomCar, TransactionSellToCustomer


admin.site.register(Showroom)
admin.site.register(ShowroomProfile)
admin.site.register(ShowroomCar)
admin.site.register(TransactionSellToCustomer)
