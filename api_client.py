import requests

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None):
        url = self.base_url + endpoint
        response = requests.get(url, params=params)
        return response

    def post(self, endpoint, data=None):
        url = self.base_url + endpoint
        response = requests.post(url, json=data)
        return response

    def put(self, endpoint, data=None):
        url = self.base_url + endpoint
        response = requests.put(url, json=data)
        return response

    def delete(self, endpoint):
        url = self.base_url + endpoint
        response = requests.delete(url)