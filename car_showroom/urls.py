from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from core.views import StatisticShowroomViewSet


from customer.views import CustomerCarList, CustomerCarDetail
from showroom.views import ShowroomCarList, ShowroomCarDetail

from showroom.views import TransactionSellToCustomerList, TransactionSellToCustomerDetail
from dealer.views import TransactionSellToShowroomList, TransactionSellToShowroomDetail

from car.views import CarList, CarDetail, CarViewSet

from customer.views import CustomerViewSet, CustomerProfileViewSet
from showroom.views import ShowroomViewSet, ShowroomProfileViewSet
from dealer.views import DealerViewSet, DealerProfileViewSet, DealerCarsViewSet

from sales.views import ShowroomSalesViewSet, DealerSalesViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from django.conf.urls.static import static
from django.conf import settings

# swagger
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()

# statistic
router.register('statistic-car', CarViewSet)
router.register('statistic-showroom', StatisticShowroomViewSet)
# router.register('users', UserViewSet)

router.register('customer', CustomerViewSet)
router.register('showroom', ShowroomViewSet)
router.register('dealer', DealerViewSet)
# profiles
router.register('customer-profile', CustomerProfileViewSet)
router.register('showroom-profile', ShowroomProfileViewSet)
router.register('dealer-profile', DealerProfileViewSet)
# many_to_many_tables
router.register('car-dealer', DealerCarsViewSet)
# sales
router.register('sales-showroom', ShowroomSalesViewSet)
router.register('sales-dealer', DealerSalesViewSet)

# swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls')),

    path('car/', CarList.as_view()),
    path('car-detail/<pk>/', CarDetail.as_view()),

    path('customer-car/', CustomerCarList.as_view()),
    path('customer-car/<pk>/', CustomerCarDetail.as_view()),

    path('showroom-car/', ShowroomCarList.as_view()),
    path('showroom-car/<pk>/', ShowroomCarDetail.as_view()),

    path('dealer-transaction/', TransactionSellToShowroomList.as_view()),
    path('dealer-transaction/<pk>/', TransactionSellToShowroomDetail.as_view()),

    path('showroom-transaction/', TransactionSellToCustomerList.as_view()),
    path('showroom-transaction/<pk>/', TransactionSellToCustomerDetail.as_view()),
    # JWT
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # Djoser
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

]

# swagger
urlpatterns += [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
