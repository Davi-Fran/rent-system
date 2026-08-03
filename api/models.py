from django.db import models

class Property(models.Model):
    title = models.CharField()
    property_type = models.CharField(max_length=100)
    rent_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)
    address = models.CharField()
    cep = models.CharField(max_length=9)
    complement = models.CharField(max_length=100, blank=True, null=True)
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return self.title