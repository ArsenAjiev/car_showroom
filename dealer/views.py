from rest_framework import viewsets, mixins
from dealer.serializers import DealerSerializer, DealerProfileSerializer, DealerCarSerializer
from dealer.models import Dealer, DealerProfile, DealerCar


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
