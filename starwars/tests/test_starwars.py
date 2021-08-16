import requests  # Allows for the importing of data from the api
import pymongo as pm  # Allows access to mongodb
# Below are the app's functions that have been imported in order to test them
from starwars.app.starships_api_request import starships_api_request
from starwars.app.characters_api_request import characters_api_request
from starwars.app.list_of_pilot_names import list_of_pilot_names
from starwars.app.list_of_object_ids import list_of_object_ids
from starwars.app.add_starships_to_mongodb import add_starships_to_mongodb
from starwars.app.update_pilots_with_ids import update_pilots_with_ids


def test_starships_api_request():
    url = "https://swapi.dev/api/starships/"
    rqst = requests.get(url)
    data = rqst.json()
    # Checking to see if the len of the returned list is equal to the number of expected items from the api
    assert len(starships_api_request()) == data["count"]


def test_characters_api_request():
    url = "https://swapi.dev/api/people/"
    rqst = requests.get(url)
    data = rqst.json()
    # Checking to see if the len of the returned list is equal to the number of expected items from the api
    assert len(characters_api_request()) == data["count"]


def test_list_of_pilot_names():
    url = "https://swapi.dev/api/starships/"
    rqst = requests.get(url)
    data = rqst.json()
    names = []
    for result in data["results"]:
        for pilot in result["pilots"]:
            if pilot is not None:
                url = pilot
                rqst = requests.get(url)
                data = rqst.json()
                name = data["name"]
                names.append(name)
    assert names[0] == list_of_pilot_names()[0][0]


def test_list_of_object_ids():
    assert len(list_of_object_ids()) == len(list_of_pilot_names())


def test_add_starships_to_mongodb():
    assert add_starships_to_mongodb() == len(starships_api_request())


def test_replace_pilots_with_id():
    client = pm.MongoClient()
    db = client['starwars']
    starships_collection = db["starships"]
    first_object_id = list_of_object_ids()[0][0]
    first_starship_name = update_pilots_with_ids()[0]
    first_starship_pilot_id = []
    pilot_ids = starships_collection.find({"name": {"$eq": first_starship_name}}, {"_id": 0, "pilots": 1})
    for pilot in pilot_ids:
        first_starship_pilot_id.append(pilot)
    assert first_starship_pilot_id[0]["pilots"][0] == first_object_id
