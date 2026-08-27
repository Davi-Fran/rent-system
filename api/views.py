from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from .models import *

from .serializers import *

from .filters import UserFilter, PropertyFilter, AgreementFilter, PaymentFilter

from django_filters.rest_framework import DjangoFilterBackend

import matplotlib.pyplot as plt

from django.http import HttpResponse
from django.db.models import Count

from io import BytesIO


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter

    @action(
        detail=False,
        methods=["GET"],
        permission_classes=[IsAdminUser]
    )
    def names(self, request):
        users = User.objects.all()
        user_full_names = [
            user.get_full_name()
            for user in users
        ]

        return Response(user_full_names)


class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = PropertyFilter

    @action(
        detail=False,
        methods=["GET"],
        # permission_classes=[IsAdminUser]
    )
    def titles(self, request):
        propertys = Property.objects.all()
        propertys_titles = [property.title for property in propertys]

        return Response(propertys_titles)


    @action(
        detail=False,
        methods=["GET"],
    )
    def barchart(self, request):
        data = Property.objects.values("property_type").annotate(total=Count("id"))

        property_types = [item["property_type"] for item in data]
        totals = [item["total"] for item in data]

        bar_colors = ["tab:red", "tab:blue", "tab:orange"]

        plt.bar(property_types, totals, color=bar_colors)
        plt.title("Imobiliaria Longitude")
        plt.xlabel("Tipos")
        plt.ylabel("Totais")

        image = BytesIO()

        plt.savefig(image, format="png")
        plt.close()

        image.seek(0)

        return HttpResponse(image, content_type="image/png")

    @action(
        detail=False,
        methods=["GET"],
    )
    def piechart(self, request):
        data = Property.objects.values("property_type").annotate(total=Count("id"))

        property_types = [item["property_type"] for item in data]
        totals = [item["total"] for item in data]

        image = BytesIO()

        plt.pie(
            totals, 
            labels=property_types, 
            autopct="%1.1f%%",
            colors=["yellow", "lightblue", "pink"]
        )

        plt.savefig(image, format="png")
        plt.close()

        image.seek(0)

        return HttpResponse(image, content_type="image/png")


class AgreementViewSet(ModelViewSet):
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = AgreementFilter

    @action(
        detail=False,
        methods=["GET"],
        permission_classes=[IsAdminUser]
    )
    def details(self, request):
        agreements = Agreement.objects.all()
        agreements_details = [
            {
                "agreement_number": agreement.id,
                "renter_full_name": agreement.renter.get_full_name(),
                "lessor_full_name": agreement.lessor.get_full_name()
            }
            for agreement in agreements
        ]

        return Response(agreements_details)


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = PaymentFilter

    @action(
        detail=False,
        methods=["GET"],
        permission_classes=[IsAdminUser]
    )
    def details(self, request):
        payments = Payment.objects.all()
        payments_detail = [
            {
                "lessor": payment.agreement.lessor.get_full_name(),
                "price": payment.price,
                "payment_date": payment.payment_date
            }
            for payment in payments
        ]

        return Response(payments_detail)