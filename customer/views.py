from rest_framework import viewsets, mixins
from customer.serializers import CustomerSerializer, CustomerProfileSerializer, CustomerCarSerializer
from customer.models import Customer, CustomerProfile, CustomerCar

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.permissions import IsCustomer


# use viewsets.GenericViewSet and Mixin
class CustomerViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = Customer.customer_obj.all()
    serializer_class = CustomerSerializer


# use viewsets.GenericViewSet and Mixin
class CustomerProfileViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin

):
    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerProfileSerializer
    # permission_classes = (IsCustomer,)

    # def perform_create(self, serializer):
    #     """Create a new customer profile"""
    #     serializer.save(user=self.request.user)


# use base APIView
class CustomerCarList(APIView):
    """ List of customer's car"""

    def get(self, request):
        items = CustomerCar.objects.all()
        serializer = CustomerCarSerializer(items, many=True)
        return Response(serializer.data)


# use base APIView
class CustomerCarDetail(APIView):
    """ item of customer's car"""

    def get_object(self, pk):
        try:
            return CustomerCar.objects.get(pk=pk)
        except CustomerCar.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        item = self.get_object(pk)
        serializer = CustomerCarSerializer(item)
        return Response(serializer.data)

