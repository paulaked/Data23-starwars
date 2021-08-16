import pymongo
import requests
from starships_data import import_data

client = pymongo.MongoClient()
db = client['starwars']


def test_created_starship():
    import_data()
    assert "starships" in db.list_collection_names()

def test_matching_data():
    for i in range(1, 80):
        if requests.head('https://swapi.dev/api/starships/%i/' % i).status_code == 200:
            resp = requests.get('https://swapi.dev/api/starships/%i/' % i)
            data = resp.json()
            test_entry = db.starships.find_one({"name":data["name"]},{"_id":0, "name":1})
            assert test_entry is not None
