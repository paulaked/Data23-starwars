from pymongo import MongoClient
from app.setup_db import setup_collections
from app.update_collection import replace_url_with_id

if __name__ == '__main__':
    client = MongoClient('mongodb://localhost:27017/')
    db = client['starwars']

    setup_collections('characters', 'https://swapi.dev/api/people')
    setup_collections('starships', 'https://swapi.dev/api/starships')

    # Update pilots list from url to objectid
    replace_url_with_id()
