from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class AgreementViewSet(ModelViewSet):
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer