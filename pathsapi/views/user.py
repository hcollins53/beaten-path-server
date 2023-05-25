from django.contrib.auth.models import User
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

class UserView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type
        """
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        users = User.objects.all()
        
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = User
        fields = ('id', "first_name", "last_name", "username")