from rest_framework import viewsets, mixins
from customer.serializers import CustomerSerializer, CustomerProfileSerializer, CustomerCarSerializer
from customer.models import Customer, CustomerProfile, CustomerCar


class CustomerViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = Customer.customer_obj.all()
    serializer_class = CustomerSerializer


class CustomerProfileViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.generics.RetrieveUpdateAPIView

):
    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerProfileSerializer

    def perform_create(self, serializer):
        """Create a new customer"""
        serializer.save(user=self.request.user)


class CustomerCarViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin

):
    queryset = CustomerCar.objects.all()
    serializer_class = CustomerCarSerializer
