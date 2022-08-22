from rest_framework import viewsets, mixins
from showroom.serializers import ShowroomSerializer, ShowroomCarSerializer, ShowroomProfileSerializer
from showroom.models import Showroom, ShowroomCar, ShowroomProfile
from showroom.models import TransactionSellToCustomer
from showroom.serializers import TransactionSellToCustomerSerializer



class ShowroomViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = Showroom.showroom_obj.all()
    serializer_class = ShowroomSerializer


class ShowroomCarViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin

):
    queryset = ShowroomCar.objects.all()
    serializer_class = ShowroomCarSerializer


class ShowroomProfileViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.generics.RetrieveUpdateAPIView

):
    queryset = ShowroomProfile.objects.all()
    serializer_class = ShowroomProfileSerializer


class TransactionSellToCustomerViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = TransactionSellToCustomer.objects.all()
    serializer_class = TransactionSellToCustomerSerializer
