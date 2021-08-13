from API_class import Api
import unittest


class ApiTests(unittest.TestCase):

    api_test = Api("https://swapi.dev/api/")

    def test_a_status_code(self):
        self.assertEqual(self.api_test.status_code, 200)

    def test_b_json(self):
        self.assertEqual(type(self.api_test.json), dict)

    def test_c_url(self):
        self.assertEqual(self.api_test.url, "https://swapi.dev/api/")

    def test_d_get(self):
        self.assertEqual(str(self.api_test.get(self.api_test.url)), '<Response [200]>')

    starship_test = Api("https://swapi.dev/api/starships/")

    def test_e_starships_url(self):
        self.assertEqual(self.starship_test.url, "https://swapi.dev/api/starships/")

    def test_f_starships_status(self):
        self.assertEqual(self.starship_test.status_code, 200)

    def test_g_starships_results(self):
        self.assertEqual(type(self.starship_test.results()), list)
        self.assertEqual(len(self.starship_test.results()), 36)

    def test_h_pilot_names(self):
        self.assertEqual(self.starship_test.pilot_name('https://swapi.dev/api/people/13/'), 'Chewbacca')
        self.assertEqual(self.starship_test.pilot_name('https://swapi.dev/api/people/15/'), 'Greedo')
        self.assertEqual(self.starship_test.pilot_name('https://swapi.dev/api/people/51/'), 'Mace Windu')

    people_test = Api("https://swapi.dev/api/people/")

    def test_i_people_url(self):
        self.assertEqual(self.people_test.url, "https://swapi.dev/api/people/")

    def test_j_people_status(self):
        self.assertEqual(self.people_test.status_code, 200)

    def test_k_people_results(self):
        self.assertEqual(len(self.people_test.results()), 82)

