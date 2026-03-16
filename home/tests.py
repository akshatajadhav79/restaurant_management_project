from rest_framework.test import APITestCase
from rest_framework import status
from home.models import Restaurant

class RestaurantInfoAPITest(APITestCase):
    def test_get_resturant_info(self):
        restaurant = Restaurant.objects.create(name = "Test Restaurant",address = "123 Test st")
        response = self.client.get('/api/restaurant-info/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'],restaurant.name)
        self.assertEqual(response.data[0]['address'],restaurant.address)