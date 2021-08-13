from collection_class import *
import unittest


class CollectionTests(unittest.TestCase):

    col_test = Collection()

    def test_a_client(self):
        self.assertEqual(self.col_test.client.list_database_names(), ['admin', 'config', 'films', 'local', 'sparta', 'starwars'])

    def test_b_db(self):
        self.assertEqual(self.col_test.db.list_collection_names(), ['characters', 'starships'])

    char_test = Characters()

    def test_c_name(self):
        self.assertEqual(self.char_test.name, "characters")

    def test_d_size(self):
        self.assertEqual(self.char_test.size, 87)

    def test_e_content(self):
        self.assertEqual(type(self.char_test.content), dict)
        self.assertEqual(type(self.char_test.content['Darth Vader']), dict)
        self.assertEqual(self.char_test.content['Ackbar']['eye_color'], 'orange')

    def test_f_search(self):
        self.assertEqual(self.char_test.search('Luke Skywalker'), 'ObjectId("6113b535b103dc95f7e6903e")')
        self.assertEqual(self.char_test.search('Yoda'), 'ObjectId("6113b5683f828072dc446189")')

    star_test = Starships()

    def test_h_name(self):
        self.assertEqual(self.star_test.name, "starships")

    def test_i_insert(self):
        test_doc = {'name': 'death star', 'capacity': 1000}
        self.star_test.insert(test_doc)
        self.assertEqual(self.star_test.search('death star')['capacity'], 1000)

    def test_j_clear(self):
        self.star_test.clear()
        self.assertEqual(self.star_test.db.starships.estimated_document_count(), 0)
