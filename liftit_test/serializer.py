from .models import Vehicle, Owner
from rest_framework import serializers

class VehicleSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name', read_only=True)
    type_name = serializers.CharField(source='type.name', read_only=True)
    #owner = serializers.CharField(source='%s - %s'%('owner.number_document','owner.type_document'),read_only=True)
    owner_document_type = serializers.CharField(source='owner.type_document.name', read_only=True)
    owner_document_number = serializers.CharField(source='owner.number_document', read_only=True)

    class Meta:
        model = Vehicle
        fields = ('license_plate','brand_name','type_name','owner_document_type','owner_document_number')