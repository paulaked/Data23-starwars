import pymongo as pm
from starwars.app.starships_api_request import starships_api_request


def add_starships_to_mongodb():
    starships = starships_api_request()
    client = pm.MongoClient()
    db = client['starwars']
    cols = db.list_collection_names()

    if "starships" not in cols:
        starships_collection = db["starships"]
        insert_docs = starships_collection.insert_many(starships)
        number_of_inserted = len(insert_docs.inserted_ids)
        return number_of_inserted
    else:
        number_of_inserted = len(starships_api_request())
        return number_of_inserted
