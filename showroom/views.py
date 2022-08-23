from rest_framework import viewsets, mixins
from showroom.serializers import ShowroomSerializer, ShowroomCarSerializer, ShowroomProfileSerializer
from showroom.models import Showroom, ShowroomCar, ShowroomProfile
from showroom.models import TransactionSellToCustomer
from showroom.serializers import TransactionSellToCustomerSerializer

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from core.permissions import IsShowroom


# use viewsets.GenericViewSet and Mixin
class ShowroomViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = Showroom.showroom_obj.all()
    serializer_class = ShowroomSerializer


# use base APIView
class ShowroomCarList(APIView):
    """ List of showroom's car"""
    def get(self, request):
        item = ShowroomCar.objects.all()
        serializer = ShowroomCarSerializer(item, many=True)
        return Response(serializer.data)


# use base APIView
class ShowroomCarDetail(APIView):
    """ Item of showroom's car"""

    def get_object(self, pk):
        try:
            return ShowroomCar.objects.get(pk=pk)
        except ShowroomCar.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        item = self.get_object(pk)
        serializer = ShowroomCarSerializer(item)
        return Response(serializer.data)


# use viewsets.GenericViewSet and Mixin
class ShowroomProfileViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin

):
    queryset = ShowroomProfile.objects.all()
    serializer_class = ShowroomProfileSerializer
    # permission_classes = (IsShowroom, )


# # use generics.ListAPIView
class TransactionSellToCustomerList(generics.ListAPIView):
    queryset = TransactionSellToCustomer.objects.all()
    serializer_class = TransactionSellToCustomerSerializer


# use generics.RetrieveAPIView
class TransactionSellToCustomerDetail(generics.RetrieveAPIView):
    queryset = TransactionSellToCustomer.objects.all()
    serializer_class = TransactionSellToCustomerSerializer
    lookup_field = 'pk'


