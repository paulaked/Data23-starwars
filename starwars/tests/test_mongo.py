import pytest
from app.init_mongodb import mongo_setup

def drop_test():
    db = mongo_setup()
    db.starships.update_one({"test":"foo"})
    mongo_setup()
    assert db.starship.stats(scale) == 0