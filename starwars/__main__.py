
if __name__ == '__main__':
    import pymongo
    import requests
    from pprint import pprint
    from app.replace_pilots import replace_pilots
    from app.starships_data import import_data

    client = pymongo.MongoClient()
    db = client['starwars']

    import_data()
    replace_pilots()
    all_starships = db.starships.find({})
    for starship in all_starships:
        pprint(starship)