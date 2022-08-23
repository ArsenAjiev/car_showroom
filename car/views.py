from car.serializers import CarSerializer
from car.models import Car
from django_filters.rest_framework import DjangoFilterBackend
from core.filters import CarFilter
from rest_framework import permissions, generics, viewsets, mixins
from core.permissions import IsCustomer, IsDealer, IsShowroom
from rest_framework.response import Response
from rest_framework.decorators import action

from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


class CarList(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CarFilter
    # permission_classes = (permissions.IsAuthenticated,)


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CarFilter
    # permission_classes = (permissions.IsAuthenticated,)


class CarViewSet(viewsets.GenericViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

    @action(detail=False, methods=['get'], url_path='car-static')
    def car_static(self, request):
        car_count = Car.objects.filter(is_active=True).count()
        content = {'car_count': car_count}
        return Response(content)