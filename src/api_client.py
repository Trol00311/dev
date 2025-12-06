import requests

class ApiClient:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://webexapis.com/v1"

    def list_rooms(self):
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(f"{self.base_url}/rooms", headers=headers)
        return response

    def create_room(self, name):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        payload = {"title": name}
        response = requests.post(f"{self.base_url}/rooms", json=payload, headers=headers)
        return response

    def get_room_details(self, room_id):
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        url = f"{self.base_url}/rooms/{room_id}"
        response = requests.get(url, headers=headers)
        return response
