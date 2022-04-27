from rest_framework.serializers import ModelSerializer
from buildings.models import Building

class BuildingSerializer(ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'