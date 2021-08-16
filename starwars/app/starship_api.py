# here we will start making our api calling functions

import requests
import json
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['starwars']
col = db["starships"]


def clear_starships():
    db.starships.delete_many({})

def api_call(url):  # this is to check that our api call works
    response = requests.get(url)
    return response

def crawl_api(url):  # this is to get the results of our api
    response = requests.get(url)
    api_results = json.loads(response.content)
    for item in api_results['results']:
        yield item
    if 'next' in api_results and api_results['next'] is not None:
        next_page = crawl_api(api_results['next'])
        for page in next_page:
            yield page

def api_api(url):  #this to to get results where there is no next
    response = requests.get(url)
    api_results = (response.json())
    return api_results

def mongo_api_url(url):  # take in url and return names
    response = requests.get(url)
    api_results = (response.json())
    return api_results['name']

def mongdb_name_id(name):  #this is to get all the names and object ids from the characters part
    name_id = db.characters.find({'name': name}, {'name': 1, '_id': 1})
    for ni in name_id:
        return ni



