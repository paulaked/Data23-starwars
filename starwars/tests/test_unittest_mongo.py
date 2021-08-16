import unittest
import starwars.app.mongoFunctions as mb

class MongoTest(unittest.TestCase):


    mb.db.starships.delete_many({})
    collection = mb.db.starships.count()
    mb.db.starships.insert_one({'one': 'onee'})
    collection2 = mb.db.starships.count()
    id_and_name_list = []
    mb.add_details_to_list(mb.db.characters.find({}),id_and_name_list, 'name', '_id')

    # test successful empty of a collection
    def test_delete_files_from_collection(self):
        self.assertEqual(self.collection, 0)

    # test adding to a collection
    def test_add_one_to_collection(self):
        self.assertEqual(self.collection2, 1)

    # Test creating list from collection
    def test_add_name_and_id_to_list(self):
        self.assertEqual(len(self.id_and_name_list),87)

    # Test if first name in new list is Ackbar
    def test_first_name_details(self):
        self.assertEqual(self.id_and_name_list[0][0],'Ackbar')

    # Test if last name in new list is Zam Wessel
    def test_last_name_details(self):
        self.assertEqual(self.id_and_name_list[-1][0], 'Zam Wesell')






