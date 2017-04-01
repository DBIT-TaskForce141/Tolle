from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=10, unique=True)
    dob = models.DateField(blank=True, null=True)


class Wallet(models.Model):
    user = models.OneToOneField(User)
    wallet_balance = models.FloatField(default=0)


class WalletTransaction(models.Model):
    TRANSACTION_CHOICES = (
        ('Credit', 'Credit'),
        ('Debit', 'Debit'),
    )
    wallet = models.OneToOneField(Wallet)
    transaction_type = models.CharField(max_length=30, choices=TRANSACTION_CHOICES)
    transaction_date_time = models.DateTimeField(default=datetime.now())
    recipient = models.CharField(max_length=300)
    amount = models.FloatField()


class RfidCar(models.Model):
    rfid_no = models.CharField(max_length=20, unique=True)
    number_plate = models.CharField(max_length=10, null=False, unique=True, default="")
    car_name = models.CharField(max_length=20)
    car_type = models.CharField(max_length=20)
    chassis_no = models.CharField(max_length=20)
    issue_date = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.chassis_no


class UserRfid(models.Model):
    user = models.ForeignKey(User)
    rfid_no = models.OneToOneField(RfidCar, unique=True)

    def __str__(self):
        return self.rfid_no.rfid_no


class TollPlaza(models.Model):
    toll_name = models.CharField(max_length=100, default="")
    toll_latitude = models.FloatField()
    toll_longitude = models.FloatField()
    three_wheeler_toll = models.IntegerField()
    car_jeep_van_toll = models.IntegerField()
    lcv_minibus_toll = models.IntegerField()
    truck_bus_toll = models.IntegerField()
    heavy_vehicle_toll = models.IntegerField()


class Transaction(models.Model):
    transaction_no = models.CharField(max_length=20)
    rfid_no = models.ForeignKey(RfidCar)
    toll = models.ForeignKey(TollPlaza, default="")
    transaction_date_time = models.DateTimeField(blank=True, null=True)
    amount_paid = models.IntegerField(default=0)
    payment_status = models.BooleanField(default=False)

class Service(models.Model):
    service_name = models.CharField(max_length=50)

class serviceAt(models.Model):
    service = models.ForeignKey(Service)
    tollPlaza = models.ForeignKey(TollPlaza)
    description = models.CharField(max_length = 150)
