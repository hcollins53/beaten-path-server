from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from pathsapi.models import Trail, Completedlist
from django.contrib.auth.models import User

class CompletedListView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type
        """
        try:
            complete = Completedlist.objects.get(pk=pk)
            serializer = CompletedlistSerializer(complete)
            return Response(serializer.data)
        except Trail.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        completes = Completedlist.objects.all()
        serializer = CompletedlistSerializer(completes, many=True)
        return Response(serializer.data)
    def create(self, request):
        """Handle POST operations
            Returns
            Response -- JSON serialized game instance
        """
        serializer = CreateCompletedlistSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        complete = Completedlist.objects.get(pk=pk)
        trail = Trail.objects.get(pk=request.data["trail"])
        complete.trail = trail
        user = User.objects.get(pk=request.data["user"])
        complete.user = user
        complete.date = request.data["date"]
        #self.check_object_permissions(request, trail)
        complete.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    def destroy(self, request, pk):
        
        complete = Completedlist.objects.get(pk=pk)
        #self.check_object_permissions(request, trail)
        complete.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
class CreateCompletedlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Completedlist
        fields = ['id', 'trail', 'user', 'date']   
class CompletedlistSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Completedlist
        fields = ('id', 'trail', 'user', 'date')