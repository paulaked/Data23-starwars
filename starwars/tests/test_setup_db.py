import pytest
import pymongo
from app.setup_db import setup_collections, get_data

def test_get_data():
    url = 'https://swapi.dev/api/people'
    all_people_data = get_data(url)

    # Check all documents form characters is returned i.e. 82
    assert len(all_people_data) == 82

    url = 'https://swapi.dev/api/starships'
    all_starships_data = get_data(url)

    # Check all documents form starships is returned i.e. 36
    assert len(all_people_data) == 36



def test_setup_collections():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['starwars']

    setup_collections('characters', 'https://swapi.dev/api/people')
    setup_collections('starships', 'https://swapi.dev/api/starships')

    # Test characters and starship collection have been created
    assert 'characters' in db.list_collection_names()
    assert 'starship' in db.list_collection_names()
    
    # Test a character that exist is in the collection
    char = db.characters.find_one({'name': 'Darth Vader'})
    assert char['name'] == 'Darth Vader'

    # Test a starship that exist is in the collection
    ship = db.starship.find_one({'name': 'Star Destroyer'})
    assert char['name'] == 'Star Destroyer'
