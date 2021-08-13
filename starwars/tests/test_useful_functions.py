from useful_functions import replace
from API_class import Api
import unittest


class MainTests(unittest.TestCase):

    starships_request = Api("https://swapi.dev/api/starships/")
    starships = starships_request.results()

    def test_a_replace(self):
        replace(self.starships[0], self.starships_request)
        self.assertEqual(self.starships[0]['pilots'], [])

        replace(self.starships[4], self.starships_request)
        self.assertEqual(str(self.starships[4]['pilots']), "[ObjectId('6113b515b631f43f2faff030'), "
                                                           "ObjectId('6113b52750a7cf9e064de7ac'), "
                                                           "ObjectId('6113b532019c4c8ad0c7000e'), "
                                                           "ObjectId('6113b53b908d50cfe30092f8')]")

        replace(self.starships[7], self.starships_request)
        self.assertEqual(str(self.starships[7]['pilots']), "[ObjectId('6113b51987f3c4eb3eeb8817')]")

