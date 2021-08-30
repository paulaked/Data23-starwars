from pymongo import MongoClient
import requests

def get_data(url):
    # Get all data from API
    response = requests.get(url).json()
    data = response['results']
    # Get data if there is more in new page
    while response['next'] is not None:
        response = requests.get(response['next']).json()
        data.extend(response['results'])

    return data

def setup_collections(collection, url, client=None):
    # Setup db
    client = client or MongoClient('mongodb://localhost:27017/')
    db = client['starwars']

    # Drop the db to repopulate later
    db[collection].drop()

    # Get data from url
    data = get_data(url)

    # Insert the data in the collection
    db[collection].insert_many(data)
    print('-' * 100)
    print(f'Dropped and added {collection} collections')
    print('-' * 100)

if __name__ == '__main__':
    setup_collections('characters', 'https://swapi.dev/api/people')
    setup_collections('starships', 'https://swapi.dev/api/starships')