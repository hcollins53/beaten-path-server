from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from pathsapi.models import Message
from django.contrib.auth.models import User

class MessageView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type
        """
        try:
            message = Message.objects.get(pk=pk)
            serializer = MessageSerializer(message)
            return Response(serializer.data)
        except Message.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        messages = Message.objects.all()
        sender_id = request.query_params.get('sender', None)
        receiver_id = request.query_params.get('receiver', None)
        if sender_id is not None:
            user = User.objects.get(pk=sender_id)
            messages = Message.objects.filter(sender=user.id)
        if receiver_id is not None:
            user = User.objects.get(pk=receiver_id)
            messages = Message.objects.filter(receiver=user.id)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
    def create(self, request):
        """Handle POST operations
            Returns
            Response -- JSON serialized game instance
        """
        serializer = CreateMessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        message = Message.objects.get(pk=pk)
        sender = User.objects.get(pk=request.data["sender"])
        message.sender = sender
        receiver = User.objects.get(pk=request.data["receiver"])
        message.receiver = receiver
        message.body = request.data["body"]
        message.date = request.data["date"]
        #self.check_object_permissions(request, trail)
        message.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    def destroy(self, request, pk):
        
        message = Message.objects.get(pk=pk)
        #self.check_object_permissions(request, trail)
        message.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
class CreateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'body', 'date']   
class MessageSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Message
        fields = ('id', 'sender', 'receiver', 'body', 'date')