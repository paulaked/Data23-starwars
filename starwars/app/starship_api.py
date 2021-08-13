# here we will start making our api calling functions

import requests
import json
import pymongo
from pprint import pprint as pp


client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['starwars']
col = db["starships"]


def crawl_starships(url):
    response = requests.get(url)
    api_results = json.loads(response.content)
    for starship in api_results['results']:
        yield starship
    if 'next' in api_results and api_results['next'] is not None:
        next_page = crawl_starships(api_results['next'])
        for page in next_page:
            yield page

stsh = crawl_starships("https://swapi.dev/api/starships")
for result in stsh:
    list_starships = []
    list_starships.append(result)
    pp(list_starships)
    x = col.insert_one(result)
    print(x)


