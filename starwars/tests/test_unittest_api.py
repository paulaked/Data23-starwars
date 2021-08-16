import unittest
import starwars.app.apiFunctions as api

class ApiTest(unittest.TestCase):

    req = api.requests.get('https://swapi.dev/api/starships/')
    collection = []
    api.extract_from_page(req,collection)
    collection2 = []
    api.extract_until_null('https://swapi.dev/api/starships/', collection2)

    # Test if the link can be accessed
    def test_connection(self):
        self.assertEqual(self.req.status_code, 200)

    # Test if the results are successfully accessed
    def test_extract_from_page(self):
        self.assertEqual(self.req.json()['results'][0]['name'],  "CR90 corvette")

    # Test if record can be added to the list
    def test_add_file_to_list(self):
        self.assertEqual(len(self.collection), 10)

    # Test if all ships from all pages get added
    def test_add_all_files_to_list(self):
        self.assertEqual(len(self.collection2), 36)
