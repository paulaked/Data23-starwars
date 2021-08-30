import pytest
import pymongo
from app.update_collection import find_char_url, replace_url_with_id

def test_find_char_url():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['starwars']

    char = db.characters.find_one({'name': 'Darth Vader'})
    assert 'https://swapi.dev/api/people/4/' in char['url']

