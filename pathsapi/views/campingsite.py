from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from pathsapi.models import Trail, CampingSite


class CampingSiteView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type
        """
        try:
            campingsite = CampingSite.objects.get(pk=pk)
            serializer = CampingSiteSerializer(campingsite)
            return Response(serializer.data)
        except Trail.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        campingsites = CampingSite.objects.all()
        trail_id = request.query_params.get('trail', None)
        if trail_id is not None:
            trail = Trail.objects.get(pk=trail_id)
            campingsites = CampingSite.objects.filter(trail=trail)
        serializer = CampingSiteSerializer(campingsites, many=True)
        return Response(serializer.data)
    def create(self, request):
        """Handle POST operations
            Returns
            Response -- JSON serialized game instance
        """
        serializer = CreateCampingSiteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        campingsite = CampingSite.objects.get(pk=pk)
        campingsite.name = request.data["name"]
        trail = Trail.objects.get(pk=request.data["trail"])
        campingsite.trail = trail
        campingsite.distance = request.data["distance"]
        campingsite.fees = request.data["fees"]
        campingsite.site = request.data["site"]
        #self.check_object_permissions(request, trail)
        campingsite.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    def destroy(self, request, pk):
        
        campingsite = CampingSite.objects.get(pk=pk)
        #self.check_object_permissions(request, trail)
        campingsite.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
class CreateCampingSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampingSite
        fields = ['id', 'name', 'trail', 'distance', 'fees', 'site']   
class CampingSiteSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = CampingSite
        fields = ('id', 'name', 'trail', 'distance', 'fees', 'site')