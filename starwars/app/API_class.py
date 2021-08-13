import requests


class Api:

    def __init__(self, url: str):
        self.url = url
        self.status_code = self.get().status_code
        self.json = self.get().json()

    def get(self):
        return requests.get(self.url)

    def results(self):
        full_list = self.get().json()['results']
        url = self.url
        while self.get().json()['next'] is not None:
            self.url = self.get().json()['next']
            full_list += self.get().json()['results']
        self.url = url
        return full_list
