from pymongo import MongoClient

def find_char_url(url, collection='characters', client=None):
    client = client or MongoClient('mongodb://localhost:27017/')
    db = client['starwars']

    # Get object id of each character by their URL
    id = db[collection].find_one({'url': url}, {'_id': 1})['_id']
    return id

def replace_url_with_id(client=None):
    client = client or MongoClient('mongodb://localhost:27017/')
    db = client['starwars']
    for starship in db.starships.find({}):
        pilots = starship['pilots']

        if pilots:
            pilot_ids = []
            for url in pilots:
                pilot_ids.append(find_char_url(url))

            print('.' * 100)
            print(f'Pilots URLs: {pilots}')
            print(f'Pilots ids: {pilot_ids}')

            db.starships.update_one(starship, {'$set': {'pilots': pilot_ids}})
