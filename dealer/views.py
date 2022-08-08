from rest_framework import viewsets, mixins
from dealer.serializers import DealerSerializer, DealerProfileSerializer, DealerCarSerializer
from dealer.serializers import TransactionSellToShowroomSerializer
from dealer.models import Dealer, DealerProfile, DealerCar, TransactionSellToShowroom


class DealerViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = Dealer.dealer_obj.all()
    serializer_class = DealerSerializer


class DealerProfileViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.generics.RetrieveUpdateAPIView

):
    queryset = DealerProfile.objects.all()
    serializer_class = DealerProfileSerializer

    def perform_create(self, serializer):
        """Create a new customer"""
        serializer.save(user=self.request.user)


class DealerCarViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.generics.RetrieveUpdateAPIView

):
    queryset = DealerCar.objects.all()
    serializer_class = DealerCarSerializer


class TransactionSellToShowroomViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = TransactionSellToShowroom.objects.all()
    serializer_class = TransactionSellToShowroomSerializer
