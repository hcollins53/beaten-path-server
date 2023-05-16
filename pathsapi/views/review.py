from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from pathsapi.models import Review, Trail
from django.contrib.auth.models import User


class ReviewView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type
        """
        try:
            review = Review.objects.get(pk=pk)
            serializer = ReviewSerializer(review)
            return Response(serializer.data)
        except Review.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    def create(self, request):
        """Handle POST operations
            Returns
            Response -- JSON serialized game instance
        """
        serializer = CreateReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        review = Review.objects.get(pk=pk)
        review.title = request.data["title"]
        trail = Trail.objects.get(pk=request.data["trail"])
        review.trail = trail
        user = User.objects.get(pk=request.data["user"])
        review.user = user
        review.description = request.data["description"]
        review.rating = request.data["rating"]
        review.img = request.data["img"]
        review.date = request.data["date"]
        #self.check_object_permissions(request, trail)
        review.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    def destroy(self, request, pk):
        
        review = Review.objects.get(pk=pk)
        #self.check_object_permissions(request, review)
        review.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'title', 'trail', 'user', 'description', 'rating', 'img', 'date']   
class ReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Review
        fields = ('id', 'title', 'trail', 'user', 'description', 'rating', 'date', 'img')