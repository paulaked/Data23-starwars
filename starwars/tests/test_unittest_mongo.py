import unittest
import starwars.app.mongoFunctions as mb

class MongoTest(unittest.TestCase):


    mb.db.starships.delete_many({})
    collection = mb.db.starships.count()
    mb.db.starships.insert_one({'one': 'onee'})
    collection2 = mb.db.starships.count()

    def test_delete_files_from_collection(self):
        self.assertEqual(self.collection, 0)

    def test_add_to_collection(self):
        self.assertEqual(self.collection2, 1)





