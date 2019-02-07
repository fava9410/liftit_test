from .models import Vehicle, Owner
from rest_framework import serializers

class VehicleSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name', read_only=True)
    type_name = serializers.CharField(source='type.name', read_only=True)

    class Meta:
        model = Vehicle
        fields = ('license_plate','brand_name','type_name')