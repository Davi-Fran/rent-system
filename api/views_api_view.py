from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User, Property, Agreement, Payment
from .serializers import UserSerializer, PropertySerializer, AgreementSerializer, PaymentSerializer


# CRUD Usuários
class UsersRouteAPIView(APIView):
    def get(self, request):
        users = User.objects.all().order_by("id")
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsersDetailAPIView(APIView):
    def get_object(self, pk):
        return User.objects.get(pk=pk)


    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)

        return Response(serializer.data)


    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


# CRUD Imóveis
class PropertysRouteAPIView(APIView):
    def get(self, request):
        propertys = Property.objects.all()
        serializer = PropertySerializer(propertys, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        newProperty = PropertySerializer(data=request.data)

        if newProperty.is_valid():
            newProperty.save()

            return Response(newProperty.data, status=status.HTTP_201_CREATED)

        return Response(newProperty.errors, status=status.HTTP_400_BAD_REQUEST)

class PropertysDetailAPIView(APIView):
    def get_property(self, pk):
        return Property.objects.get(pk=pk)

    def get(self, request, pk):
        property = self.get_property(pk)
        serializer = PropertySerializer(property)

        return Response(serializer.data)

    def put(self, request, pk):
        property = self.get_property(pk)
        serializer = PropertySerializer(property, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        property = self.get_property(pk)
        property.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


# CRUD Contratos
class AgreementsRouteAPIView(APIView):
    def get(self, request):
        agreements = Agreement.objects.all()
        serializer = AgreementSerializer(agreements, many=True)

        return Response(serializer.data)

    def post(self, request):
        newAgreement = AgreementSerializer(data=request.data)

        if newAgreement.is_valid():
            newAgreement.save()

            return Response(newAgreement.data, status=status.HTTP_201_CREATED)

        return Response(newAgreement.errors, status=status.HTTP_400_BAD_REQUEST)

class AgreementsDetailAPIView(APIView):
    def get_agreement(self, pk):
        return Agreement.objects.get(pk=pk)
    
    def get(self, request, pk):
        agreement = self.get_agreement(pk)
        serializer = AgreementSerializer(agreement)
    
        return Response(serializer.data)
    
    def put(self, request, pk):
        agreement = self.get_agreement(pk)
        serializer = AgreementSerializer(agreement, data=request.data)
    
        if serializer.is_valid():
            serializer.save()
    
            return Response(serializer.data)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        agreement = self.get_agreement(pk)
        agreement.delete()
    
        return Response(status=status.HTTP_204_NO_CONTENT)


# CRUD Pagamentos
class PaymentsRouteAPIView(APIView):
    def get(self, request):
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)

        return Response(serializer.data)

    def post(self, request):
        newPayment = PaymentSerializer(data=request.data)

        if newPayment.is_valid():
            newPayment.save()

            return Response(newPayment.data, status=status.HTTP_201_CREATED)

        return Response(newPayment.errors, status=status.HTTP_400_BAD_REQUEST)

class PaymentsDetailAPIView(APIView):
    def get_payment(self, pk):
        return Payment.objects.get(pk=pk)

    def get(self, request, pk):
        payment = self.get_payment(pk)
        serializer = PaymentSerializer(payment)

        return Response(serializer.data)

    def put(self, request, pk):
        payment = self.get_payment(pk)
        serializer = PaymentSerializer(payment, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        payment = self.get_payment(pk)
        payment.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)