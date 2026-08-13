from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class UserType(models.TextChoices):
        ADMIN = "ADMIN", "Administrator"
        USER = "USER", "User"

    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    user_type = models.CharField(
        max_length=20,
        choices=UserType.choices,
        default=UserType.USER
    )

    def __str__(self):
        return self.get_full_name() or self.username


class Property(models.Model):
    title = models.CharField(max_length=254)
    property_type = models.CharField(max_length=100, blank=False, null=False)
    rent_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)
    address = models.TextField()
    cep = models.CharField(max_length=9)
    complement = models.CharField(max_length=100, blank=True, null=True)
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return self.title


class Agreement(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)
    lessor = models.ForeignKey(
        User,
        related_name="lessor",
        on_delete=models.DO_NOTHING
    )
    renter = models.ForeignKey(
        User,
        related_name="renter",
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return f"Agreement {self.id}"


class Payment(models.Model):
    payment_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField()
    agreement = models.ForeignKey(
        Agreement,
        on_delete=models.DO_NOTHING,
        related_name="agreement"
    )

    def __str__(self):
        return f"Payment No. {self.id}"