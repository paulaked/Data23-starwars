import unittest
import starship_api

class ttd(unittest.TestCase):  # creat a class to test everything

    def api_connection_test(self):  # we need to test that we are getting a good response from api
        self.assertEqual(self.api_call, 200)  # 200 = good response

    def api_output_correct(self):  # we need to make sure we are getting all of the starship data
        self.assertEqual(self.api_len, 36)  # there are 36 starships - no more movies planned so should be good

    def mongo_connect(self):  # you want to make sure its connecting to mongodb

    def mongo_collection(self):  # you want to make sure that a starship collection is being made

    def mongo_document(self):  #check if 36 collections are being made





