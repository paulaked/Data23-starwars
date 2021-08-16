import pytest
import pymongo
from app.init_mongodb import mongo_setup

def test_drop():
    client = pymongo.MongoClient()
    db = client['starwars']
    db.create_collection("starship")
    mongo_setup()
    assert "starship" not in db.list_collection_names(), "checks that mongo_setup delets existing starship collection"

