from django.contrib import admin
from dealer.models import Dealer, DealerProfile, DealerCar, TransactionSellToShowroom


admin.site.register(Dealer)
admin.site.register(DealerProfile)
admin.site.register(DealerCar)
admin.site.register(TransactionSellToShowroom)
