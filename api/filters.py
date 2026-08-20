import django_filters

from .models import User, Property, Agreement, Payment

class UserFilter(django_filters.FilterSet):
    user_type = django_filters.CharFilter(field_name="user_type", lookup_expr="iexact")
    first_name = django_filters.CharFilter(field_name="first_name", lookup_expr="icontains")

    class Meta:
        model = User
        fields = ["user_type", "first_name"]


class PropertyFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")
    property_type = django_filters.CharFilter(field_name="property_type", lookup_expr="icontains")
    status = django_filters.NumberFilter(field_name="status", lookup_expr="exact")

    class Meta:
        model = Property
        fields = ["title", "property_type", "status"]


class AgreementFilter(django_filters.FilterSet):
    status = django_filters.NumberFilter(field_name="status", lookup_expr="exact")

    class Meta:
        model = Agreement
        fields = ["status"]


class PaymentFilter(django_filters.FilterSet):
    status = django_filters.NumberFilter(field_name="status", lookup_expr="exact")

    class Meta:
        model = Payment
        fields = ["status"]