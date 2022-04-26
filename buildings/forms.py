from django.forms import ModelForm
from .models import Building, Review


class AddBuildingForm(ModelForm):
    class Meta:
        model = Building
        fields = ["name", "location", "owner", "units_count", "tags"]

class UpdateBuildingForm(ModelForm):
    class Meta:
        model = Building
        fields = ["name", "location", "units_count"]
