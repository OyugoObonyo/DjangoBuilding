from .serializers import BuildingSerializer
from buildings.models import Building
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_all_buildings(request):
    buildings = Building.objects.all()
    serializer = BuildingSerializer(buildings, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_building(request, id):
    building = Building.objects.get(id=id)
    serializer = BuildingSerializer(building, many=False)
    return Response(serializer.data)


