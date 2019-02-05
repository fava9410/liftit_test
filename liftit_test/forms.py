from django.forms import ModelForm
from .models import Owner

class register_owner(ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'