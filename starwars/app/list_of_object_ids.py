import pymongo as pm
from starwars.app.list_of_pilot_names import list_of_pilot_names


def list_of_object_ids():
    client = pm.MongoClient()
    db = client['starwars']

    pilot_names = list_of_pilot_names()

    object_ids = []

    for name_list in pilot_names:
        temp_id_list = []
        for name in name_list:
            character = db.characters.find_one({"name": name})
            character_id = character["_id"]
            temp_id_list.append(character_id)
        object_ids.append(temp_id_list)
    return object_ids

