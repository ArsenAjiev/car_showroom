from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from car.views import CarViewSet
from customer.views import CustomerViewSet, CustomerProfileViewSet, CustomerCarViewSet
from showroom.views import ShowroomViewSet, ShowroomCarViewSet, ShowroomProfileViewSet
from dealer.views import DealerViewSet, DealerProfileViewSet, DealerCarViewSet
from dealer.views import TransactionSellToShowroomViewSet
from showroom.views import TransactionSellToCustomerViewSet
from sales.views import ShowroomSalesViewSet, DealerSalesViewSet


router = DefaultRouter()


router.register('car', CarViewSet)
router.register('customer', CustomerViewSet)
router.register('showroom', ShowroomViewSet)
router.register('dealer', DealerViewSet)
router.register('customer_profile', CustomerProfileViewSet)
router.register('showroom_profile', ShowroomProfileViewSet)
router.register('dealer_profile', DealerProfileViewSet)
router.register('car_dealer', DealerCarViewSet)
router.register('car_showroom', ShowroomCarViewSet)
router.register('car_customer', CustomerCarViewSet)
router.register('sell_to_showroom', TransactionSellToShowroomViewSet)
router.register('sell_to_customer', TransactionSellToCustomerViewSet)
router.register('sales_showroom', ShowroomSalesViewSet)
router.register('sales_dealer', DealerSalesViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),


]
