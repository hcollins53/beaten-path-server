import random
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from pathsapi.models import UserProfile, Trail


class UserProfileTests(APITestCase):
    fixtures = ['users', 'tokens']
    def setUp(self):
        """
        Set up for Tests
        """
        self.user1 = User.objects.create(username="hannah", first_name="hannah", last_name="collins", email="hannah@gmail.com")
        
        self.token = Token.objects.create(user=self.user1)

        self.client.credentials(
           HTTP_AUTHORIZATION=f'Token {self.token.key}')
        
        
        self.userprofile = UserProfile.objects.create(user=self.user1.id, image="https://thumbs.dreamstime.com/b/nature-river-side-photography-nd-some-random-clicks-78857225.jpg",
                                                      favorite_hike="Tubbs Hill", description="moderate", area="CDA")

    def test_create_userprofile(self):
        """
        Ensure we can create a new userprofile.
        """
       
        data = {
            "user": self.user1.id,
            "image": "https://thumbs.dreamstime.com/b/nature-river-side-photography-nd-some-random-clicks-78857225.jpg",
            "favorite_hike": "Tubbs Hill",
            "description": "moderate",
            "area": "CDA",
            
        }
        response = self.client.post('/userprofiles', data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data['id'])


    # def test_update_userprofile(self):
    #     """
    #     Ensure we can update a trail.
    #     """
    #     userprofile = self.userprofile
        
    #     data = {
    #         "user": self.user1.id,
    #         "image": "https://thumbs.dreamstime.com/b/nature-river-side-photography-nd-some-random-clicks-78857225.jpg",
    #         "favorite_hike": "Tubbs Hill",
    #         "description": "helloooooo",
    #         "area": "CDA",
            
    #     }
    #     response = self.client.put(f'/userprofiles/{userprofile.id}', data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    #     userprofile_updated = UserProfile.objects.get(pk=userprofile.id)
    #     self.assertEqual(userprofile_updated.description, data['description'])

    # def test_get_all_userprofiles(self):
    #     """
    #     Ensure we can get a collection of trails.
    #     """
    #     response = self.client.get('/userprofiles')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data), UserProfile.objects.count())
    # def test_delete_trail(self):
    #     """testing if it deletes a trail"""
    #     userprofile = UserProfile.objects.first()
    #     response = self.client.delete(f'/userprofiles/{userprofile.id}')
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)