from API_class import Api
import unittest


class ApiTests(unittest.TestCase):

    api_test = Api("https://swapi.dev/api/")

    # test to check if the API get request was successful
    def test_a_status_code(self):
        self.assertEqual(self.api_test.status_code, 200)

    # test to see if the json variable is of the correct datatype
    def test_b_json(self):
        self.assertEqual(type(self.api_test.json), dict)

    # test to see if the url variable is storing the correct information
    def test_c_url(self):
        self.assertEqual(self.api_test.url, "https://swapi.dev/api/")

    # test to see if the get method produces a successful response
    def test_d_get(self):
        self.assertEqual(str(self.api_test.get(self.api_test.url)), '<Response [200]>')

    starship_test = Api("https://swapi.dev/api/starships/")

    # test to see if the url variable is storing the correct information
    def test_e_starships_url(self):
        self.assertEqual(self.starship_test.url, "https://swapi.dev/api/starships/")

    # test to check if the API get request was successful
    def test_f_starships_status(self):
        self.assertEqual(self.starship_test.status_code, 200)

    # test to see is the results method pulls data from all pages via the SWAPI
    def test_g_starships_results(self):
        self.assertEqual(type(self.starship_test.results()), list)
        self.assertEqual(type(self.starship_test.results()[0]), dict)
        self.assertEqual(len(self.starship_test.results()), 36)

    # test to see if the pilot_name method returns the correct character name
    def test_h_pilot_names(self):
        self.assertEqual(self.starship_test.pilot_name('https://swapi.dev/api/people/13/'), 'Chewbacca')
        self.assertEqual(self.starship_test.pilot_name('https://swapi.dev/api/people/15/'), 'Greedo')
        self.assertEqual(self.starship_test.pilot_name('https://swapi.dev/api/people/51/'), 'Mace Windu')

    films_test = Api("https://swapi.dev/api/films/")

    # test to see if the film_name method returns the correct film name
    def test_i_film_names(self):
        self.assertEqual(self.films_test.film_name("https://swapi.dev/api/films/1/"), "A New Hope")
        self.assertEqual(self.films_test.film_name("https://swapi.dev/api/films/4/"), "The Phantom Menace")
        self.assertEqual(self.films_test.film_name("https://swapi.dev/api/films/5/"), "Attack of the Clones")

    # test to see if the transform_films method returns the correct fields
    def test_j_transform_films(self):
        films = self.films_test.transform_films()
        self.assertEqual(list(films[0].keys()),
                         ['title', 'episode_id', 'opening_crawl', 'director', 'producer', 'release_date', 'url'])

    people_test = Api("https://swapi.dev/api/people/")

    # test to see if the url variable is storing the correct information
    def test_k_people_url(self):
        self.assertEqual(self.people_test.url, "https://swapi.dev/api/people/")

    # test to check if the API get request was successful
    def test_l_people_status(self):
        self.assertEqual(self.people_test.status_code, 200)

    # test to see is the results method pulls data from all pages via the SWAPI
    def test_m_people_results(self):
        self.assertEqual(len(self.people_test.results()), 82)
