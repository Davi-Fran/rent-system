from rest_framework import serializers

from .models import User, Property, Agreement, Payment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "telephone",
            "password"
        ]

        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def create(self, validate_data):
        password = validate_data.pop("password")

        user = User(**validate_data)
        user.set_password(password)

        user.save()
        return user


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = "__all__"


class AgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"