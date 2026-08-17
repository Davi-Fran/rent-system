from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import *
from .serializers import *


# CRUD Usuário
class UserListCreateGeneric(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyGeneric(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# CRUD Imóveis
class PropertyListCreateGeneric(ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyRetrieveUpdateDestroyGeneric(RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


# CRUD Contratos
class AgreementListCreateGeneric(ListCreateAPIView):
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer

class AgreementRetrieveUpdateDestroyGeneric(RetrieveUpdateDestroyAPIView):
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer


# CRUD Pagamentos
class PaymentListCreateGeneric(ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentRetrieveUpdateDestroyGeneric(RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer