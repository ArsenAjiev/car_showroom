from showroom.models import ShowroomProfile, ShowroomCar, TransactionSellToCustomer
from showroom.serializers import ShowroomCarSerializer
from core.models import User
from core.serializers import UserSerializer

from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count


class StatisticShowroomViewSet(viewsets.GenericViewSet):
    serializer_class = ShowroomCarSerializer
    queryset = ShowroomCar.objects.all()

    @action(detail=False, methods=['get'], url_path='showroom-test')
    def showroom_test(self, request):
        count = ShowroomCar.objects.all().count()
        content = {'car_count': count}
        return Response(content)

    @action(detail=False, methods=['get'], url_path='showroom-stat')
    def showroom_stat(self, request):
        if not request.user.pk:
            return Response({'Message': "Need authorization"})
        else:
            # showroom instance
            sh = ShowroomProfile.objects.get(user_id=request.user.pk)
            # showroom_profile instance
            query = TransactionSellToCustomer.objects.filter(showroom_id=sh)
            # car count
            q = query.values('customer_id').annotate(total_cars=Count('id'))
            content = {'customers': q}
            return Response(content)



class UserViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
