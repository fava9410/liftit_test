from django.forms import ModelForm
from .models import Owner, Vehicle

class register_owner_form(ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'

class register_vehicle_form(ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'