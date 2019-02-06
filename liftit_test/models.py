from django.db import models
import os

class Type_Document(models.Model):
    name = models.CharField(max_length = 20)

def iddocument_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s-%s.%s' % (instance.type_document.name,instance.number_document, ext)
    return os.path.join('iddocuments', filename)

class Owner(models.Model):
    number_document = models.CharField(max_length = 14, primary_key = True)
    type_document = models.ForeignKey(Type_Document, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    iddocument_file = models.FileField(upload_to=iddocument_path)

class Vehicle_Type(models.Model):
    name = models.CharField(max_length = 20)

class Vehicle_Brand(models.Model):
    name = models.CharField(max_length = 20)

class Vehicle(models.Model):
    license_plate = models.CharField(max_length = 8, primary_key = True)
    brand = models.ForeignKey(Vehicle_Brand, on_delete=models.CASCADE)
    type = models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
