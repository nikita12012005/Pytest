import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_hotels(self):
        response = requests.get(f"{self.base_url}/hotels")
        return response.json()
