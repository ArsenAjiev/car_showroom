from django.contrib import admin
from customer.models import Customer, CustomerProfile, CustomerCar


admin.site.register(Customer)
admin.site.register(CustomerProfile)
admin.site.register(CustomerCar)
