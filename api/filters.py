import django_filters

from .models import User, Property, Agreement, Payment



""" 
    exact = valor exato
    iexact = valor exato, porém ignorando o case
    contains = se contem o valor procurado
    icontains = se contem o valor procurado, porém ignorando o case
    gt = greater than (maior que)
    gte = greather than or equal (maior ou igual a)
    lt = less than (menor que)
    lte = less than or equal (menor ou igual a)
"""



class UserFilter(django_filters.FilterSet):
    user_type = django_filters.CharFilter(field_name="user_type", lookup_expr="iexact")
    first_name = django_filters.CharFilter(field_name="first_name", lookup_expr="icontains")

    class Meta:
        model = User
        fields = ["user_type", "first_name"]


class PropertyFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")
    property_type = django_filters.CharFilter(field_name="property_type", lookup_expr="icontains")
    rent_price = django_filters.NumberFilter(field_name="rent_price", lookup_expr="gte")
    status = django_filters.BooleanFilter(field_name="status", lookup_expr="exact")

    class Meta:
        model = Property
        fields = ["title", "property_type", "rent_price", "status"]


class AgreementFilter(django_filters.FilterSet):
    status = django_filters.BooleanFilter(field_name="status", lookup_expr="exact")
    start_date = django_filters.DateFilter(field_name="start_date", lookup_expr="gte")
    end_date = django_filters.DateFilter(field_name="end_date", lookup_expr="lte")
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    lessor = django_filters.NumberFilter(field_name="lessor_id")

    class Meta:
        model = Agreement
        fields = ["status", "start_date", "end_date", "price", "renter_id"]


class PaymentFilter(django_filters.FilterSet):
    status = django_filters.BooleanFilter(field_name="status", lookup_expr="exact")
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    payment_date = django_filters.DateFilter(field_name="payment_date")

    class Meta:
        model = Payment
        fields = ["status", "price", "payment_date"]