from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from pathsapi.models import Trail, Wantlist
from django.contrib.auth.models import User

class WantListView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type
        """
        try:
            
            wishlist = Wantlist.objects.get(pk=pk)
            serializer = WantListSerializer(wishlist)
            return Response(serializer.data)
        except Trail.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        wishlists = Wantlist.objects.all() 
        user_id = request.query_params.get('user', None)
        if user_id is not None:
            user = User.objects.get(pk=user_id)
            wishlists = Wantlist.objects.filter(user=user)
         
        serializer = WantListSerializer(wishlists, many=True)
        return Response(serializer.data)
    def create(self, request):
        """Handle POST operations
            Returns
            Response -- JSON serialized game instance
        """
        serializer = CreateWantListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        wishlist = Wantlist.objects.get(pk=pk)
        trail = Trail.objects.get(pk=request.data["trail"])
        wishlist.trail = trail
        user = User.objects.get(pk=request.data["user"])
        wishlist.user = user
        #self.check_object_permissions(request, trail)
        wishlist.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    def destroy(self, request, pk):
        
        wishlist = Wantlist.objects.get(pk=pk)
        #self.check_object_permissions(request, trail)
        wishlist.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
class CreateWantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wantlist
        fields = ['id', 'trail', 'user']   
class WantListSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Wantlist
        fields = ('id', 'trail', 'user')
        depth = 1