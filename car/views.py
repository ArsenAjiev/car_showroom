from rest_framework import viewsets, mixins
from car.serializers import CarSerializer
from car.models import Car


class CarViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
