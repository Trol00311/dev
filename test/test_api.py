import unittest
from unittest.mock import patch
from src.api_client import ApiClient

class TestApiClient(unittest.TestCase):

    @patch("src.api_client.requests.get")
    def test_list_rooms_success(self, mock_get):
        # Przygotowanie mocka
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"items": []}

        # Wywołanie metody
        api = ApiClient("dummy")
        response = api.list_rooms()

        # Assercje
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"items": []})
    
  @patch("src.api_client.requests.get")
    def test_list_rooms_unauthorized(self, mock_get):
        mock_get.return_value.status_code = 401

        api = ApiClient("dummy")
        response = api.list_rooms()

        self.assertEqual(response.status_code, 401)

    @patch("src.api_client.requests.post")
    def test_create_room_success(self, mock_post):
        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = {"title": "LAB Room"}

        api = ApiClient("dummy")
        response = api.create_room("LAB Room")

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["title"], "LAB Room")

