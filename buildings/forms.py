from dataclasses import fields
from django.forms import ModelForm
from .models import Building


class AddBuildingForm(ModelForm):
    class Meta:
        model = Building
        fields = '__all__'

class UpdateBuildingForm(ModelForm):
    class Meta:
        model = Building
        fields = ["name", "location", "units_count"]