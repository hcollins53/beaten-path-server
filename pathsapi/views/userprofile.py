from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from pathsapi.models import UserProfile
from django.contrib.auth.models import User

class UserProfileListView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type
        """
        try:
            profile = UserProfile.objects.get(pk=pk)
            serializer = UserProfileSerializer(profile)
            return Response(serializer.data)
        except UserProfile.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        profiles = UserProfile.objects.all()
        user_id = request.query_params.get('user', None)
        if user_id is not None:
            user = User.objects.get(pk=user_id)
            profiles = UserProfile.objects.filter(user=user.id)
        serializer = UserProfileSerializer(profiles, many=True)
        return Response(serializer.data)
    def create(self, request):
        """Handle POST operations
            Returns
            Response -- JSON serialized game instance
        """
        serializer = CreateUserProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        profile = UserProfile.objects.get(pk=pk)
        profile.image = request.data["image"]
        profile.favorite_hike = request.data["favorite_hike"]
        profile.description = request.data["description"]
        profile.area = request.data["area"]
        #self.check_object_permissions(request, trail)
        profile.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    def destroy(self, request, pk):
        
        profile = UserProfile.objects.get(pk=pk)
        #self.check_object_permissions(request, trail)
        profile.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
class CreateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'image', 'favorite_hike', 'description', 'area']   
class UserProfileSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'image', 'favorite_hike', 'description', 'area')
        depth = 1