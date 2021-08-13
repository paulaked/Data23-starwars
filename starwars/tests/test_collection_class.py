from collection_class import *
import unittest


class CollectionTests(unittest.TestCase):

    col_test = Collection()

    # test to see if the client has been connected to correctly
    def test_a_client(self):
        self.assertEqual(self.col_test.client.list_database_names(), ['admin', 'config', 'films', 'local', 'sparta', 'starwars'])

    # test to see if the correct database has been connected to
    def test_b_db(self):
        self.assertEqual(self.col_test.db.list_collection_names(), ['characters', 'starships'])

    char_test = Characters()

    # test to see if the name of the collection is correct
    def test_c_name(self):
        self.assertEqual(self.char_test.name, "characters")

    # test to see if the size of the collection is correct
    def test_d_size(self):
        self.assertEqual(self.char_test.size, 87)

    # test to see if all the data from the collection has been imported correctly
    def test_e_content(self):
        self.assertEqual(type(self.char_test.content), dict)
        self.assertEqual(type(self.char_test.content['Darth Vader']), dict)
        self.assertEqual(self.char_test.content['Ackbar']['eye_color'], 'orange')

    # test to see if the correct objectIDs are returned for each character
    def test_f_search(self):
        self.assertEqual(str(self.char_test.search('Luke Skywalker')), "6113b535b103dc95f7e6903e")
        self.assertEqual(str(self.char_test.search('Yoda')), "6113b5683f828072dc446189")

    star_test = Starships()

    # test to see if the name of the collection is correct
    def test_h_name(self):
        self.assertEqual(self.star_test.name, "starships")

    # test to see if the insert function correctly inserts a document into the starship collection
    def test_i_insert(self):
        test_doc = {'name': 'death star', 'capacity': 1000}
        test_doc2 = {'name': 'TIE fighter', 'pilot name': 'Darth Vader'}
        self.star_test.insert(test_doc)
        self.star_test.insert(test_doc2)
        self.assertEqual(type(self.star_test.search('death star')), dict)
        self.assertEqual(self.star_test.search('death star')['capacity'], 1000)
        self.assertEqual(self.star_test.search('TIE fighter')['pilot name'], 'Darth Vader')

    # test to see if the clear function deletes all documents from the collection
    def test_j_clear(self):
        self.star_test.clear()
        self.assertEqual(self.star_test.size, 0)
