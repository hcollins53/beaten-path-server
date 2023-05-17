import random
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from pathsapi.models.trail import Trail

class TrailTests(APITestCase):
    def setUp(self):
        """
        Set up for ProductTests
        """
        self.user1 = User.objects.get(pk=1)
        self.token = Token.objects.get(user=self.user1)

        self.client.credentials(
           HTTP_AUTHORIZATION=f'Token {self.token.key}')

       # self.trail = Trail.objects.first()

    def test_create_trail(self):
        """
        Ensure we can create a new trail.
        """

        data = {
            "name": "Wolf Trail",
            "length": 3.5,
            "elevationGain": 324,
            "difficulty": "moderate",
            "lat": 48.19024,
            "lon": -117.05302,
            "img": "https://outthereoutdoors.com/wp-content/uploads/2021/05/view-from-Wolf-Trails--rotated.jpeg",
            "permit": "No",
            "fees": "free"
        }
        response = self.client.post('/trails', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data['id'])


    def test_update_trail(self):
        """
        Ensure we can update a trail.
        """
        trail = Trail.objects.first()
        data = {
            "name": trail.name,
            "length": trail.length,
            "elevationGain": trail.description,
            "difficulty": trail.difficulty,
            "lat": trail.lat,
            "lon": trail.lon,
            "img": trail.img,
            "permit": trail.permit,
            "fees": trail.fees
        }
        response = self.client.put(f'/trails/{trail.id}', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        trail_updated = Trail.objects.get(pk=trail.id)
        self.assertEqual(trail_updated.name, data['name'])

    def test_get_all_trails(self):
        """
        Ensure we can get a collection of trails.
        """
        response = self.client.get('/trails')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Trail.objects.count())
    def test_delete_trail(self):
        """testing if it deletes a trail"""
        trail = Trail.objects.first()
        response = self.client.delete(f'/trails/{trail.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)