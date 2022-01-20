# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Auto(models.Model):
    vin = models.CharField(primary_key=True, max_length=17)
    color = models.CharField(max_length=20)
    number = models.CharField(max_length=9)
    model = models.ForeignKey('AutoProperties', models.DO_NOTHING, db_column='model')

    class Meta:
        managed = True
        db_table = 'auto'


class AutoProperties(models.Model):
    model = models.CharField(primary_key=True, max_length=20)
    brand = models.CharField(max_length=20)
    class_field = models.IntegerField(db_column='class')  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'auto_properties'


class Clients(models.Model):
    client_id = models.AutoField(primary_key=True)
    details = models.ForeignKey('PaymentDetails', models.DO_NOTHING)
    name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    telephone_number = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'clients'


class Drivers(models.Model):
    driver_id = models.AutoField(primary_key=True)
    details = models.ForeignKey('PaymentDetails', models.DO_NOTHING)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(blank=True, null=True)
    gender = models.IntegerField()
    vin = models.ForeignKey(Auto, models.DO_NOTHING, db_column='vin')

    class Meta:
        managed = False
        db_table = 'drivers'


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Clients, models.DO_NOTHING)
    sum = models.IntegerField()
    departure_longitude = models.FloatField()
    departure_latitude = models.FloatField()
    arrival_longitude = models.FloatField()
    arrival_latitude = models.FloatField()
    driver = models.ForeignKey(Drivers, models.DO_NOTHING)
    state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orders'


class PaymentDetails(models.Model):
    details_id = models.AutoField(primary_key=True)
    card_number = models.CharField(max_length=16)
    cvc = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'payment_details'
