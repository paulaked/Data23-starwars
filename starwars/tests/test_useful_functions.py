from useful_functions import *
from API_class import Api
from collection_class import Films
import unittest


class MainTests(unittest.TestCase):

    starships_request = Api("https://swapi.dev/api/starships/")
    films_request = Api("https://swapi.dev/api/films/")
    starships = starships_request.results()
    films_col = Films()

    def test_a_replace_pilots(self):
        replace_pilots(self.starships[0], self.starships_request)
        self.assertEqual(self.starships[0]['pilots'], [])

        replace_pilots(self.starships[4], self.starships_request)
        self.assertEqual(str(self.starships[4]['pilots']), "[ObjectId('6113b515b631f43f2faff030'), "
                                                           "ObjectId('6113b52750a7cf9e064de7ac'), "
                                                           "ObjectId('6113b532019c4c8ad0c7000e'), "
                                                           "ObjectId('6113b53b908d50cfe30092f8')]")

        replace_pilots(self.starships[7], self.starships_request)
        self.assertEqual(str(self.starships[7]['pilots']), "[ObjectId('6113b51987f3c4eb3eeb8817')]")

    def test_b_replace_films(self):
        films = self.films_request.transform_films()
        for film in films:
            self.films_col.insert(film)

        replace_films(self.starships[0], self.starships_request, self.films_col)
        query = self.films_col.db.films.find(
            {"title": {"$in": ['A New Hope', "Return of the Jedi", "Revenge of the Sith"]}}, {"_id": 1})
        result = []
        for item in query:
            result.append(item['_id'])
        self.assertEqual(self.starships[0]['films'], result)

        replace_films(self.starships[4], self.starships_request, self.films_col)
        query = self.films_col.db.films.find(
            {"title": {"$in": ['A New Hope', "Return of the Jedi", "The Empire Strikes Back"]}}, {"_id": 1})
        result = []
        for item in query:
            result.append(item['_id'])
        self.assertEqual(self.starships[4]['films'], result)

        self.films_col.clear()
