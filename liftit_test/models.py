from django.db import models

class Type_Document(models.Model):
    name = models.CharField(max_length = 20)

class Owner(models.Model):
    number_document = models.CharField(max_length = 14, primary_key = True)
    type_document = models.ForeignKey(Type_Document, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)

class Vehicle_Type(models.Model):
    name = models.CharField(max_length = 20)
    #description = models.CharField(max_length = 50)

class Vehicle_Brand(models.Model):
    name = models.CharField(max_length = 20)
    #description = models.CharField(max_length = 50)

class Vehicle(models.Model):
    license_plate = models.CharField(max_length = 8, primary_key = True)
    brand = models.ForeignKey(Vehicle_Brand, on_delete=models.CASCADE)
    type = models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)
    #owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
