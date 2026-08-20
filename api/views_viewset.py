from rest_framework.viewsets import ModelViewSet

from .models import *

from .serializers import *

from .filters import UserFilter, PropertyFilter, AgreementFilter, PaymentFilter

from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter


class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = PropertyFilter


class AgreementViewSet(ModelViewSet):
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = AgreementFilter


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = PaymentFilter