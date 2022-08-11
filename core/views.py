from rest_framework import viewsets, mixins
from core.serializers import UserSerializer
from core.models import User


class UserViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer

