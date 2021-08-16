import pymongo
import requests
from replace_pilots import replace_pilots
from starships_data import import_data

client = pymongo.MongoClient()
db = client['starwars']

def test_replace_pilots():
    db.drop_collection("starships")
    import_data()
    replace_pilots()
    pilot_object = db.starships.find({},{"pilots":1, "_id":0})
    for pilot in pilot_object:
        for id in pilot["pilots"]:
            print(id)
            assert "https://swapi.dev/api/" not in str(id)

test_replace_pilots()
