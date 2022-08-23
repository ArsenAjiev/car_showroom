from rest_framework import viewsets, mixins
from dealer.serializers import DealerSerializer, DealerProfileSerializer, DealerCarSerializer
from dealer.serializers import TransactionSellToShowroomSerializer
from dealer.models import Dealer, DealerProfile, DealerCar, TransactionSellToShowroom

from rest_framework import generics

from core.permissions import IsDealer


# use viewsets.GenericViewSet and Mixin
class DealerViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = Dealer.dealer_obj.all()
    serializer_class = DealerSerializer


# use viewsets.GenericViewSet and Mixin
class DealerProfileViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin

):
    queryset = DealerProfile.objects.all()
    serializer_class = DealerProfileSerializer
    # permission_classes = (IsDealer, )

    # def perform_create(self, serializer):
    #     """Create a new customer"""
    #     serializer.save(user=self.request.user)


class DealerCarsViewSet(viewsets.ModelViewSet):
    queryset = DealerCar.objects.all()
    serializer_class = DealerCarSerializer


# use generics.ListAPIView
class TransactionSellToShowroomList(generics.ListAPIView):
    queryset = TransactionSellToShowroom.objects.all()
    serializer_class = TransactionSellToShowroomSerializer


# use generics.RetrieveAPIView
class TransactionSellToShowroomDetail(generics.RetrieveAPIView):
    queryset = TransactionSellToShowroom.objects.all()
    serializer_class = TransactionSellToShowroomSerializer
    lookup_field = 'pk'


