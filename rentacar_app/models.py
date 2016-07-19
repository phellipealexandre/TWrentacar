from django.db import models

class Car(models.Model):
    model = models.CharField(max_length=200)
    plate = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    price_per_day = models.FloatField()

class Customer(models.Model):
    name = models.CharField(max_length=200)
    cpf = models.CharField(max_length=200)
    birthday = models.DateField()

class Rent(models.Model):
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    rent_date = models.DateField()
    numberOfRentalDays = models.IntegerField()
    real_delivery_date = models.DateField(null=True, blank=True)
    total_price = models.FloatField(null=True, blank=True)
