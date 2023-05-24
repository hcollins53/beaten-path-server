from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from pathsapi.models import Trail


class TrailView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type
        """
        try:
            trail = Trail.objects.get(pk=pk)
            serializer = TrailSerializer(trail)
            return Response(serializer.data)
        except Trail.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        trails = Trail.objects.all()
        difficulty_id = request.query_params.get('difficulty', None)
        length_id = request.query_params.get('length', None)
        elevationGain_id = request.query_params.get('elevationGain', None)
        title = request.query_params.get('title', None)
        if difficulty_id is not None:
            trails = Trail.objects.filter(difficulty=difficulty_id)
        if length_id is not None:
            if length_id == "3":
                max_length = 3
                trails = Trail.objects.filter(length__lte=max_length)
            if length_id == "6":
                min_length = 3
                max_length = 6
                trails = Trail.objects.filter(length__gte=min_length, length__lte=max_length)
            if length_id == "6.1":
                min_length = 6
                trails = Trail.objects.filter(length__gte=min_length)
        if elevationGain_id is not None:
            if elevationGain_id == "700":
                max_elevationGain = 700
                trails = Trail.objects.filter(elevationGain__lte=max_elevationGain)
            elif elevationGain_id == "1500":
                min_elevationGain = 700
                max_elevationGain = 1500
                trails = Trail.objects.filter(elevationGain__gte=min_elevationGain, elevationGain__lte=max_elevationGain)
            elif elevationGain_id == "1501":
                min_elevationGain = 1500
                trails = Trail.objects.filter(elevationGain__gte=min_elevationGain)
        if title is not None:
            trails = Trail.objects.filter(name__icontains = title)
        serializer = TrailSerializer(trails, many=True)
        return Response(serializer.data)
    def create(self, request):
        """Handle POST operations
            Returns
            Response -- JSON serialized game instance
        """
        serializer = CreateTrailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        trail = Trail.objects.get(pk=pk)
        trail.name = request.data["name"]
        trail.length = request.data["length"]
        trail.elevationGain = request.data["elevationGain"]
        trail.difficulty = request.data["difficulty"]
        trail.lat = request.data["lat"]
        trail.lon = request.data["lon"]
        trail.img = request.data["img"]
        trail.permit = request.data["permit"]
        trail.fees = request.data["fees"]
        #self.check_object_permissions(request, trail)
        trail.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    def destroy(self, request, pk):
        
        trail = Trail.objects.get(pk=pk)
        #self.check_object_permissions(request, trail)
        trail.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
class CreateTrailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trail
        fields = ['id', 'name', 'length', 'elevationGain', 'difficulty', 'lat', 'lon', 'img', 'permit', 'fees']   
class TrailSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Trail
        fields = ('id', 'name', 'length', 'elevationGain', 'difficulty', 'lat', 'lon', 'img', 'permit', 'fees')