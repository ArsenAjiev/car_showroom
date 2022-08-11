from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from car.views import CarViewSet
from core.views import UserViewSet
from customer.views import CustomerViewSet, CustomerProfileViewSet, CustomerCarViewSet
from showroom.views import ShowroomViewSet, ShowroomCarViewSet, ShowroomProfileViewSet
from dealer.views import DealerViewSet, DealerProfileViewSet, DealerCarViewSet


router = DefaultRouter()


router.register('car', CarViewSet)
router.register('user', UserViewSet)
router.register('customer', CustomerViewSet)
router.register('showroom', ShowroomViewSet)
router.register('dealer', DealerViewSet)
router.register('customer_profile', CustomerProfileViewSet)
router.register('showroom_profile', ShowroomProfileViewSet)
router.register('dealer_profile', DealerProfileViewSet)
router.register('car_dealer', DealerCarViewSet)
router.register('car_showroom', ShowroomCarViewSet)
router.register('car_customer', CustomerCarViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),


]
