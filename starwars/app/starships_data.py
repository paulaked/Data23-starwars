# importing required packages and setting up connection to database
import pymongo
import requests

client = pymongo.MongoClient()
db = client['starwars']
base_url = 'https://swapi.dev/api/'

# imports raw data from url to collection in database
def import_data():
    # deletes any pre-existing collections called starships
    db.drop_collection("starships")
    # creating new starships collection
    starships = db["starships"]
    # iterates through 80 entries and inserts an entry when data is returned
    for i in range(1, 81):
        if requests.head('https://swapi.dev/api/starships/%i/' %i).status_code == 200:
            resp = requests.get('https://swapi.dev/api/starships/%i/' % i)
            data = resp.json()
            starships.insert_one(data)
