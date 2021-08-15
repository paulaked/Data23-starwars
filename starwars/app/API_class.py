import requests


class Api:

    def __init__(self, url: str):
        self.url = url
        self.status_code = self.get(self.url).status_code
        self.json = self.get(self.url).json()

    # uses the get request to pull data using the SWAPI
    def get(self, url: str):
        return requests.get(url)

    # used to access the results of an API request after adding an endpoint e.g. 'starships' or 'people'
    def results(self):
        full_list = self.get(self.url).json()['results']
        url = self.url
        while self.get(self.url).json()['next'] is not None:
            self.url = self.get(self.url).json()['next']
            full_list += self.get(self.url).json()['results']
        self.url = url
        return full_list

    # returns the name of the person who matches the API url request
    def pilot_name(self, url):
        return self.get(url).json()['name']

    # removes all unwanted fields from the films data
    def transform_films(self):
        films = self.results()
        for film in range(len(films)):
            for field in ['characters', 'planets', 'species', 'starships', 'vehicles', 'created', 'edited']:
                films[film].pop(field)
        return films

    def film_name(self, url):
        return self.get(url).json()['title']
