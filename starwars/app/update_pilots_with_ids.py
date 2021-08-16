import pymongo as pm
from starwars.app.list_of_object_ids import list_of_object_ids
from starwars.app.starships_api_request import starships_api_request
from starwars.app.add_starships_to_mongodb import add_starships_to_mongodb


def update_pilots_with_ids():
    add_starships_to_mongodb()
    starships = starships_api_request()

    object_ids = list_of_object_ids()
    starships_names = []

    for starship in starships:
        if not starship["pilots"]:
            continue
        else:
            starships_names.append(str(starship["name"]))

    client = pm.MongoClient()
    db = client['starwars']
    query = db.starships.find({"name": {"$in": starships_names}})

    for i in range(0, len(object_ids)):
        db["starships"].update_one({"name": query[i]["name"]}, {"$set": {"pilots": object_ids[i]}})

    query = db.starships.find({"name": {"$in": starships_names}})
    return starships_names
