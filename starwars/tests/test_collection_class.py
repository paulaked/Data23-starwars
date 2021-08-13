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

    star_test = Starships()

    def test_f_name(self):
        self.assertEqual(self.star_test.name, "starships")

    def test_i_clear(self):
        self.star_test.clear()
        self.assertEqual(self.star_test.size, 0)
